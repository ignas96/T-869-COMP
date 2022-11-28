import cv2
import numpy as np

def canny_edges(frame,threshold1,threshold2):
    edges = cv2.Canny(frame,threshold1,threshold2)
    cv2.imshow('Edges',edges)
    edge_points = np.argwhere(edges != 0)
    return edge_points

def random_points(all_points):
    if len(all_points) !=0 :
        rand1 = np.random.randint(0, len(all_points)-1)
        rand2 = np.random.randint(0, len(all_points)-1)
        p1x = all_points[rand1][0]
        p1y =all_points[rand1][1]
        p2x = all_points[rand2][0]
        p2y=all_points[rand2][1]
        return (p1x,p1y), (p2x,p2y)
    else:
        return (0,0), (0,0)

def line_equation(p1,p2):

    # y = bx + c
    b=0
    if (p2[0]-p1[0]) != 0:
        b = (p2[1]-p1[1])/(p2[0]-p1[0]) # slope of line

    # c = y - bx 
    c = p2[1]- (b*p2[0]) # intersection of y axis

    return b, -1, c

def distance_from_line(p,A,B,C):
    # print(p)
    # print(A)
    # print(B)
    # print(C)
    # d= abs(A*p[x]+B*p[y]+C)/((A^2+b^2)^(1/2))
    d = abs(A * p[0] + B * p[1] + C) / np.sqrt((A**2 + B**2))
    return d
    
def best_points(num_of_itterations, edge_points):
    num_of_points = 0
    best_p1 = (0, 0)
    best_p2 = (0, 0)

    for line in range(num_of_itterations):
        p1, p2 = random_points(edge_points)
        point_counter=0
        A,B,C = line_equation(p1,p2)
        for point in edge_points:
            if distance_from_line(point,A,B,C) < 1:
                point_counter+=1

        if (point_counter > num_of_points):
            num_of_points = point_counter
            best_p1 = p1
            best_p2 = p2
    return best_p1, best_p2

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
    if len(corners) != 4:
        # abort function if corners found are not 4
        return None

    # print(corners)
    # print(corners2)

    matrix = cv2.getPerspectiveTransform(corners, corners2)
    result = cv2.warpPerspective(quad, matrix, (400, 640))

    # display results
    #cv2.imshow("CONTOUR", contour)
    cv2.imshow('frame1', result)
    cv2.imshow("QUAD", quad)


def main():
    while(1):
        ret, frame = vid.read()
        # edge_points=canny_edges(frame,100,200)
        # p1,p2 = best_points(30,edge_points)
        # revp1 = (p1[1],p1[0])
        # revp2 = (p2[1],p2[0])
        # cv2.line(frame, revp1,revp2, (255, 0, 0), 2)
        # cv2.imshow('frame', frame)


        # image= cv2.imread("testfig.png")
        quadrangle(frame)



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    vid = cv2.VideoCapture(0)

    main()










