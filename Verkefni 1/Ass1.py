import cv2
import time
import numpy as np



# define a video capture object
vid = cv2.VideoCapture(0)

# used to record the time when we processed last frame
prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0

radius = 41
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
    # print(new_frame_time-prev_frame_time)
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
    # (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    # cv2.circle(frame, maxLoc, 1, (255, 0, 0), 2)
    ################  Bright spot part end

    ################  Red spot part start
    # image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # lower = np.array([0, 150, 255])
    # upper = np.array([ 15, 255, 255])
    # mask = cv2.inRange(image, lower, upper)
    # (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(image[:,:,1],mask=mask)

    # cv2.circle(frame, maxLoc, 1, circleColor, circleThickness)

    ################  Red spot part end

    ################ For loop brightness method start 
    # max_value = 0
    # max_x_location=0
    # max_y_location=0

    # for x_axis in range(len(gray)):
    #     for y_axis in range(len(gray[x_axis])):
    #         if max_value < gray[x_axis,y_axis]:
    #             max_value = gray[x_axis,y_axis]
    #             max_x_location = x_axis
    #             max_y_location = y_axis
    # cv2.circle(frame, (max_y_location,max_x_location), 1, (255, 0, 0), 2)
    ################ For loop brightness method end

    ################ For loop brightness method start 
    # image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # lower = np.array([0, 150, 255])
    # upper = np.array([ 15, 255, 255])
    # mask = cv2.inRange(image, lower, upper)
    # (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(image[:,:,1],mask=mask)
    # max_value = 0
    # max_x_location=0
    # max_y_location=0

    # for x_axis in range(len(gray)):
    #     for y_axis in range(len(gray[x_axis])):
    #         if max_value < gray[x_axis,y_axis]:
    #             max_value = gray[x_axis,y_axis]
    #             max_x_location = x_axis
    #             max_y_location = y_axis
    # cv2.circle(frame, (max_y_location,max_x_location), 1, (255, 0, 0), 2)
    ################ For loop brightness method end 




    # Display the resulting frame
    cv2.imshow('frame', frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap objectq
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()