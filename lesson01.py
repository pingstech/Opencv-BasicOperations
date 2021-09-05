import cv2

img=cv2.imread("lena.jpg",1)
img2=cv2.imread("lena.jpg",0)
img3=cv2.imread("lena.jpg",-1)
cv2.imshow("Image1",img)
cv2.imshow("Image2",img2)
cv2.imshow("Image3",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()