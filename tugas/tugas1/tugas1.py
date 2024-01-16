import cv2
import numpy as np

image = cv2.imread("MagangBayu2024-OpenCV/tugas/tugas1/tugas1.png")

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([75, 20, 20])
upper = np.array([100, 255, 255])

mask = cv2.inRange(image_hsv, lower, upper)

contours, _= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) != 0:
    for contour in contours:
        if cv2.contourArea(contour) > 300:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x,y), (x+w, y+h), (100, 255, 100), 2)

cv2.imshow("Mask", mask)
cv2.imshow("Gambar", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

