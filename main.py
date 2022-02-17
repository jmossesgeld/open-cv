import cv2
import numpy as np


def draw_circle(e, x, y, flags, param):
    if cv2.EVENT_LBUTTONDOWN == e:
        cv2.circle(img, (x, y), 100, (255, 255, 255))
        cv2.imshow("image", img)


img = np.zeros((512, 512, 3))
cv2.namedWindow("image")
cv2.imshow("image", img)
cv2.waitKey(0)
