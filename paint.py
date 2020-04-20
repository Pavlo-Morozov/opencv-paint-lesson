import cv2
import numpy as np

drawing = False # Before clicking the left mouse button, the drawing mode is disabled
def draw(event,x,y,flags,param): # Create function for drawing
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN: # Find out if the left mouse button is pressed
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), size, (b, g, r), -1) # create circle with color and size of RGB bar
                                                         # x,y - mouse coordinates
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
def nothing(x): # Empty function for Trackbars
    pass
cv2.namedWindow('image',cv2.WINDOW_NORMAL) #Create named window in opencv. WINDOW_NORMAL we can stretch
img = np.zeros((780,720,3), np.uint8) # with zeros we create black font
img[:] = 255,255,255 # make font colour white
cv2.resizeWindow('image',780,720)

'''Create track bars for every colour and size of the brush'''
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('Size','image',8,200,nothing)


cv2.setMouseCallback('image',draw)
while(1):
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF # Close window if we press ESC key
    if key ==27:
        break
    r = cv2.getTrackbarPos('R','image') # Update colours and size
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    size = cv2.getTrackbarPos('Size', 'image')

cv2.destroyAllWindows()
