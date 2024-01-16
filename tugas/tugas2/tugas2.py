import cv2
import numpy as np

image = cv2.imread("MagangBayu2024-OpenCV/tugas/tugas2/tugas2.jpg")

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([110, 20, 20])
upper = np.array([120, 255, 255])

mask = cv2.inRange(image_hsv, lower, upper)

canny = cv2.Canny(mask, 10, 25)

contours, _= cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    if 5000 < cv2.contourArea(contour) < 40000:
        cv2.drawContours(image, [contour], -1, (0, 0, 0), 2)
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True) #Douglas-Peucker algorithm

        cv2.putText(image, str(len(approx)), (10, 125), cv2.FONT_HERSHEY_SIMPLEX, 5, (0 ,0, 0), 2, cv2.LINE_AA)

cv2.imshow("Gambar", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

