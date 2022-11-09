import cv2
import numpy as np

img = cv2.imread("lines6.jpg")
img_org = cv2.imread("lines6.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.blur(gray,(2,2))

ret,thresh = cv2.threshold(blur,195,300,cv2.THRESH_BINARY) 

edges = cv2.Canny(thresh,100,200,apertureSize=5)

lines = cv2.HoughLinesP(edges,1,np.pi/180,1)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2) 
    #cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2) komutunda çizgiler kalın olduğu için şeritten taşmış ve içi boyanmış gibi görünebilir en sondaki 2 değerini 1 yapılırsa şeritlerden taşmadığı görülecektir.

cv2.imshow("original",img_org)
cv2.imshow("lines",img)

cv2.waitKey()
cv2.destroyAllWindows()