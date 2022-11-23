import cv2
import time
import numpy as np

def canny_edges(frame,threshold1,threshold2):
    edges = cv2.Canny(frame,threshold1,threshold2)
    cv2.imshow('Edges',edges)

def quadrangle(image):
    hh, ww = image.shape[:2]
    # convert to gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # threshold the grayscale image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    #cv2.imshow("THRESH", thresh)

    # find outer contour
    cntrs = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cntrs) == 2:
        cntrs = cntrs[0]  
    else :
        cntrs[1]
    cntr = cntrs[0]

    # draw contour on copy of img as result
    contour = image.copy()
    cv2.drawContours(contour,[cntr], 0, (0,0,255), 2)

    # limit contour to quadrilateral
    peri = cv2.arcLength(cntr, True)
    corners = cv2.approxPolyDP(cntr, 0.04 * peri, True)

    # draw quadrilateral on input image from detected corners
    quad = image.copy()
    cv2.polylines(quad, [corners], True, (0,0,255), 2, cv2.LINE_AA)
    corners2 = np.float32([[0, 0],[0, 640],[400, 640], [400, 0]])
    corners = np.float32(corners[:,0,:])
    # print(corners)
    # print(corners2)

    matrix = cv2.getPerspectiveTransform(corners, corners2)
    result = cv2.warpPerspective(quad, matrix, (400, 640))

    # display results
    #cv2.imshow("CONTOUR", contour)
    cv2.imshow('frame1', result)
    cv2.imshow("QUAD", quad)
    return corners



def main():
    while(1):
        ret, frame = vid.read()

        #canny_edges(frame,100,200)
        #image= cv2.imread("testfig.png")
        quadrangle(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #vid.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    vid = cv2.VideoCapture(0)

    main()










