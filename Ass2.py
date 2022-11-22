import cv2
import time
import numpy as np



# define a video capture object
vid = cv2.VideoCapture(0)

while(1):
    ret, frame = vid.read()
    ################ Canny start 

    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edges)
    k = cv2.waitKey(5) & 0xFF
    ################ Canny end


    if k == 27:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()