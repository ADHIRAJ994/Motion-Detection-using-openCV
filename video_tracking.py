import cv2 as cv
import numpy as np

def Nothing(x):
    pass

cap = cv.VideoCapture(0)

cv.namedWindow("Tracking")
# TO Create track bar always requires a dummy function 
cv.createTrackbar("LH","Tracking",0,255,Nothing)
cv.createTrackbar("LS","Tracking",0,255,Nothing)
cv.createTrackbar("LV","Tracking",0,255,Nothing)
cv.createTrackbar("UH","Tracking",255,255,Nothing)
cv.createTrackbar("US","Tracking",255,255,Nothing)
cv.createTrackbar("UV","Tracking",255,255,Nothing)

while True:
    _,frame = cap.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("LH","Tracking")
    l_s = cv.getTrackbarPos("LS","Tracking")
    l_v = cv.getTrackbarPos("LV","Tracking")

    u_h = cv.getTrackbarPos("UH","Tracking")
    u_s = cv.getTrackbarPos("US","Tracking")
    u_v = cv.getTrackbarPos("UV","Tracking")

    l_color = np.array([l_h,l_s,l_v])
    u_color = np.array([u_h,u_s,u_v])

    mask = cv.inRange(hsv, l_color, u_color) # Mask means Find all pixels whose HSV values fall between 
    #these limits, and make them white. Others stay black.
    res = cv.bitwise_and(frame, frame, mask=mask) # This only keeps the white pixels

    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)
    cv.imshow("Result", res)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()