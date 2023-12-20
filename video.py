import cv2
import numpy as np

vid = cv2.VideoCapture('doing.mp4')

cv2.namedWindow('My Window',cv2.WINDOW_KEEPRATIO)
cv2.setWindowProperty('My Window',cv2.WND_PROP_ASPECT_RATIO,cv2.WINDOW_KEEPRATIO)
cv2.setWindowProperty('My Window',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

while vid.isOpened():
    ret,frame = vid.read()

    cv2.imshow('My Window',frame)
    if cv2.waitKey(1) == ord('q'): break

vid.release()
cv2.destroyAllWindows()