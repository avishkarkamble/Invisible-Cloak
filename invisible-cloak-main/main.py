import cv2
import numpy as np
import time

# =========================
# 1. OPEN WEBCAM
# =========================

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("ERROR: Cannot open camera")
    exit()

print("Camera opened successfully")

# =========================
# 2. CAPTURE BACKGROUND
# =========================

print("\nMove completely away from the camera.")
print("Background will be captured in 10 seconds...\n")

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

# Capture background
background = None

for i in range(30):

    ret, frame = cap.read()

    if ret:
        frame = cv2.flip(frame, 1)
        background = frame.copy()

    cv2.waitKey(1)

if background is None:
    print("ERROR: Background capture failed")
    cap.release()
    exit()

print("\nBackground captured!")
print("Now wear the BLUE cloth and enter the frame.")
print("Press Q to quit.\n")

# =========================
# 3. MAIN LOOP
# =========================

while True:

    ret, frame = cap.read()

    if not ret:
        print("ERROR: Cannot read camera")
        break

    # Mirror camera
    frame = cv2.flip(frame, 1)

    # =========================
    # 4. CONVERT TO HSV
    # =========================

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # =========================
    # 5. BLUE COLOR DETECTION
    # =========================

    lower_blue = np.array([85, 40, 40])
    upper_blue = np.array([135, 255, 255])

    mask = cv2.inRange(
        hsv,
        lower_blue,
        upper_blue
    )

    # =========================
    # 6. CLEAN MASK
    # =========================

    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel,
        iterations=1
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )

    # Slightly smooth edges
    mask = cv2.GaussianBlur(
        mask,
        (5, 5),
        0
    )

    # =========================
    # 7. CLOAK AREA
    # =========================

    cloak_area = cv2.bitwise_and(
        background,
        background,
        mask=mask
    )

    # =========================
    # 8. EVERYTHING ELSE
    # =========================

    inverse_mask = cv2.bitwise_not(mask)

    person_area = cv2.bitwise_and(
        frame,
        frame,
        mask=inverse_mask
    )

    # =========================
    # 9. MAGIC ✨
    # =========================

    result = cv2.add(
        cloak_area,
        person_area
    )

    # =========================
    # 10. SHOW RESULT
    # =========================

    cv2.imshow(
        "Invisible Cloak - Magic ✨",
        result
    )

    # =========================
    # 11. QUIT
    # =========================

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q") or key == ord("Q"):
        break


# =========================
# 12. CLOSE
# =========================

cap.release()
cv2.destroyAllWindows()

print("Camera closed.")