import cv2
import time
import numpy as np

def main():
    while(1):
        ret, frame = vid.read()
        edges = cv2.Canny(frame,100,200)
        cv2.imshow('Edges',edges)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    vid = cv2.VideoCapture(0)

    main()



# define a video capture object

# while(1):
#     ret, frame = vid.read()
#     ################ Canny start 
#     edges = cv2.Canny(frame,100,200)
#     cv2.imshow('Edges',edges)
#     ################ Canny end

#     ################ Canny start 
#     ################ Canny end

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# vid.release()
# cv2.destroyAllWindows()










