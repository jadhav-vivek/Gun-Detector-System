import numpy as np
import cv2
import imutils

# Load cascade file (make sure cascade.xml is in same folder)
gun_cascade = cv2.CascadeClassifier("cascade.xml")

# Check if cascade loaded properly
if gun_cascade.empty():
    print("Error: cascade.xml not loaded. Check file location.")
    exit()

# Start webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera not accessible")
    exit()

gun_exist = False

print("Press 'q' to quit...")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to grab frame")
        break

    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns
    guns = gun_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(100, 100)
    )

    if len(guns) > 0:
        gun_exist = True

    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, "Gun Detected", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Security Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

if gun_exist:
    print("Gun detected")
else:
    print("Gun not detected")
