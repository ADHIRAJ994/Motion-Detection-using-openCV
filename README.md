# Motion Detection using OpenCV

Detect and highlight motion in real-time using Python and OpenCV.  
This project compares consecutive video frames to identify areas of movement and draws bounding boxes around them.

---

## Overview

This project demonstrates how to detect motion using **frame differencing** and **contour detection** in OpenCV.  
It works with both **live webcam feeds** and **recorded videos**.

### Features
- Real-time motion detection from webcam or video file  
- Highlights moving objects using rectangles  
- Adjustable sensitivity and area threshold  
- Simple, fast, and easy to understand  
- Lightweight — runs smoothly on most systems

---

##  Tech Stack

- **Python 3.7+**
- **OpenCV**
- **NumPy**

---

## How It Works

-> Two consecutive frames are captured.

-> The frames are converted to grayscale and blurred to remove noise.

-> The absolute difference between frames highlights changes.

-> The image is thresholded and dilated to isolate movement.

-> Contours of the moving regions are detected and outlined.
