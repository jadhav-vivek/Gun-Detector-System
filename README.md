# 🔫 Gun Detection System (OpenCV Project)

## 📌 Project Overview

This project is a real-time Gun Detection System built using Python and
OpenCV.\
It uses a Haar Cascade Classifier (`cascade.xml`) to detect guns through
a webcam video feed.

When a gun is detected: - A red rectangle is drawn around the detected
object - "Gun Detected" label appears on screen - Detection status is
printed in the terminal

------------------------------------------------------------------------

## 🎯 Features

-   Real-time webcam detection
-   Haar Cascade based object detection
-   Live video feed display
-   Press **'q'** to quit safely
-   Detection result printed in console

------------------------------------------------------------------------

## 📂 Project Structure

Gun-Detector/ │ ├── gun.py ├── cascade.xml ├── README.md

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python
-   OpenCV (cv2)
-   NumPy
-   imutils

------------------------------------------------------------------------

## 🚀 Installation & Setup

### 1️⃣ Install Required Libraries

pip install opencv-python numpy imutils

------------------------------------------------------------------------

### 2️⃣ Ensure Files Are in Same Folder

Make sure: - gun.py - cascade.xml

are in the same directory.

------------------------------------------------------------------------

### 3️⃣ Run the Program

python gun.py

------------------------------------------------------------------------

## 🖥 How It Works

1.  Loads the trained Haar cascade classifier (cascade.xml)
2.  Starts webcam using OpenCV
3.  Converts each frame to grayscale
4.  Detects guns using detectMultiScale()
5.  Draws bounding box if detected
6.  Displays live video feed

Press 'q' to exit the program.

------------------------------------------------------------------------

## ⚠ Important Notes

-   Works best in good lighting conditions
-   Accuracy depends on cascade training quality
-   For higher accuracy, deep learning models like YOLO can be used

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Add alarm sound on detection
-   Send email alert
-   Save screenshot automatically
-   Upgrade to YOLO object detection
-   Deploy as security surveillance system

------------------------------------------------------------------------

## 👤 Author

Vivek jadhav
Computer Vision & Python Enthusiast
