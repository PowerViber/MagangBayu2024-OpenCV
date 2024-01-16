import cv2
import numpy as np

def gs(image):
    # Convert ke hsv
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Definisi warna yang ingin hilang pada HSV
    lower = np.array([0, 0, 100])
    upper = np.array([180, 30, 255]) #disini saya set untuk menghilangkan yang putih saja

    mask = cv2.inRange(hsv, lower, upper)

    # invert agar jadi greenscreen soalnya sudah saya coba
    mask_inv = cv2.bitwise_not(mask)

    # input background
    background = cv2.imread("MagangBayu2024-OpenCV/tugas/tugas3/tugas3.jpg")

    # resize agar background bisa sepadan dengan ukuran frame
    background = cv2.resize(background, (image.shape[1], image.shape[0]))

    # agar background hanya muncul pada mask
    background_masked = cv2.bitwise_and(background, background, mask=mask)

    # apply mask pada frame
    result = cv2.bitwise_and(image, image, mask=mask_inv)

    # add background
    result = cv2.add(result, background_masked)

    return result

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret: break

    result = gs(frame)

    cv2.imshow("cam", result)

    if cv2.waitKey(1) == 27: break

cam.release()
cv2.destroyAllWindows() 
