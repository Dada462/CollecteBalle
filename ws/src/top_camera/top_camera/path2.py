import numpy as np
import cv2



#################Parameters#################
class Path :
    def __init__(self,click1,click2,i,scale,passage1,passage2,collect1,collect2) :
        self.click1=0
        self.click2=0
        self.i=0
        self.scale=20/1216
        self.passage1=np.array([0,4.5])
        self.passage2=np.array([0,-4.5])
        self.colect1=np.array([-9.19407895,-4.55592105])
        self.colect2=np.array([9.14473684,4.6875])

#################Parameters#################

    def pixel_to_xy(self,lin,col,img_shape):
        X=np.array([lin,col])
        n,p,_=img_shape
        return (X-np.array([p,n])/2)*scale

    def xy_to_pixel(self,x,y,img_shape):
        X=x,y
        n,p,_=img_shape
        X=np.array([int(X[0]/scale+p/2),int(X[1]/scale+n/2)])
        return X

    def path_planner(self,x,y,img):
        X=(x,y)
        n,p,_=img.shape
        if x>0:
            x,y=xy_to_pixel(x,y,img.shape)
            x0,y0=xy_to_pixel(*colect2,img.shape)
            cv2.line(img, (x0,y0),(x,y), (255,0,0), 2)
            # return colect2
        else:
            x,y=xy_to_pixel(x,y,img.shape)
            x0,y0=xy_to_pixel(*colect1,img.shape)
            # x0,y0=int(colect1[0]/scale+p/2),int(colect1[1]/scale+n/2)
            cv2.line(img, (x0,y0),(x,y), (255,0,0), 2)
            # return colect1
        # print(x0,y0)

    def click_event(self,event, x, y, flags, params):
        self.i,self.click1,self.click2
        if event == cv2.EVENT_LBUTTONDOWN:
            self.click2=self.click1
            print(self.click2)
            self.click1=np.array([x,y])
            self.i+=1
            n,p,_=img.shape
            # print((click1-np.array([p,n])/2)*scale)
            if self.i%2==1:
                cv2.circle(img, (x,y), 10, (0,0,255), 5)
                cv2.putText(img, str(self.i//2), (x,y), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255,255,0), 1, cv2.LINE_AA)
            if self.i%2==0:
                cv2.circle(img, (x,y), 10, (255,0,0), 5)
                # print(np.linalg.norm(self.click2-click1)*scale)
                cv2.putText(img, str(self.i//2-1), (x,y), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255,255,0), 1, cv2.LINE_AA)
            x,y=pixel_to_xy(x,y,img.shape)
            path_planner(x,y,img)
            cv2.imshow('image', img)

# driver function
if __name__ == "__main__":
    img = cv2.imread('top_camera/terrain_1.png', 1)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()