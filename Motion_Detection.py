import cv2 as cv

cap = cv.VideoCapture(0) 
ret, frame1 = cap.read()
ret, frame2 = cap.read()


while True:
    diff = cv.absdiff(frame1,frame2) # Calculates the diffrence between each pixels in the frame to highlight the changes.
    gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY) #Converts difference image to grayscale for easier processing.
    blur = cv.GaussianBlur(gray,(5,5),0)# To remove Noise from the image Smooths the image → reduces small noise so real movement stands out.
    _,thresh = cv.threshold(blur,20,255,cv.THRESH_BINARY) # Sepearates the image into black and white parts.Therefore white parts are movements and black parts are stable.
    Dilated = cv.dilate(thresh,None,iterations=3)#Makes the movement area thicker and more solid.
    contors,_ = cv.findContours(Dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)# Outlines the objects that are moving

    for contor in contors:
        (x,y,w,h) = cv.boundingRect(contor) # Draws a rectangle around the movement.
        if  cv.contourArea(contor)<900: # This ignores the small noise in the surroundings
            continue
        cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv.putText(frame1,"Status: {}".format('Movement'),(10,20),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    #cv.drawContours(frame1,contors,-1,(0,255,0),2)
    
    cv.imshow('Feed', frame1)
    frame1 = frame2 # Old frame becomes the new frame
    ret,frame2 = cap.read()

    if cv.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

