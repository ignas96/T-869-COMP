import cv2
import time
import numpy as np


def fps():
    pass
# define a video capture object
vid = cv2.VideoCapture(0)

# used to record the time when we processed last frame
prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0
radius = 41 #must be an odd number, or else GaussianBlur will fail
circleColor = (255, 0, 0)
circleThickness = 2

while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ################ FPS part start
    font = cv2.FONT_HERSHEY_SIMPLEX
        # time when we finish processing for this frame
    new_frame_time = time.time()

    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    # converting the fps into integer
    fps = int(fps)

    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)

    # putting the FPS count on the frame
    cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
    ################ FPS part end

    
    ################  Bright spot part start

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.circle(frame, maxLoc, 1, circleColor, circleThickness)
    ################  Bright spot part end



    # Display the resulting frame
    cv2.imshow('frame', frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()