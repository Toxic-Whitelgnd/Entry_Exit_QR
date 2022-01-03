from pyzbar.pyzbar import decode

import cv2

img = cv2.imread("random.png")
print(decode(img))