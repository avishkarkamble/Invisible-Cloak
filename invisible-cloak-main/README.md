# 🪄 Invisible Cloak using Python & OpenCV

An OpenCV-based Computer Vision project that creates an **Invisible Cloak effect** using a webcam.

The program detects a specific cloak color in real-time and replaces that region with a previously captured background, making the cloak appear invisible.

---

## 📌 Project Overview

The Invisible Cloak project demonstrates how **Computer Vision and Image Processing** can be used to create real-time visual effects.

The application:

1. Captures the background before the user enters the camera frame.
2. Continuously captures live webcam frames.
3. Converts each frame from BGR to HSV color space.
4. Detects the cloak using color segmentation.
5. Creates a mask for the cloak.
6. Removes the detected cloak region from the live frame.
7. Replaces it with the corresponding background region.
8. Displays the final invisible cloak effect.

---

## 🎯 Objectives

- Learn the basics of Computer Vision.
- Work with real-time webcam video.
- Understand HSV color space.
- Perform color-based object detection.
- Learn image masking.
- Learn background replacement.
- Perform real-time image processing using OpenCV.

---

## ✨ Features

- 🎥 Real-time webcam processing
- 🎨 Color-based cloak detection
- 🖼️ Background capture
- 🔍 HSV-based color segmentation
- 🎭 Image masking
- 🔄 Background replacement
- ⚡ Real-time visual effect
- 🧹 Noise removal using morphological operations

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Computer Vision and image processing |
| NumPy | Array and matrix operations |
| Webcam | Real-time video input |

---

## 📂 Project Structure

```text
Invisible-Cloak/
│
├── main.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── background.jpg
│
└── screenshots/
    └── invisible_cloak_demo.png