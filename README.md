# opencv-paint-lesson
Short paint lesson in opencv Python

import cv2
import numpy as np
drawing = False
def draw(event,x,y,flags,param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), size, (b, g, r), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
def nothing(x):
    pass
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = np.zeros((512,512,3), np.uint8)
img[:] = 255,255,255
cv2.resizeWindow('image',780,720)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('Size','image',8,200,nothing)
r = cv2.getTrackbarPos('R', 'image')
g = cv2.getTrackbarPos('G', 'image')
b = cv2.getTrackbarPos('B', 'image')

size = cv2.getTrackbarPos('Size', 'image')
