import cv2
import numpy as np


img1 = cv2.imread("smile.png")
img2 = cv2.imread("pikachu.png")
img3 = cv2.imread("pikachuforest.png")

#merges two images
"""weight = cv2.addWeighted(img1,0.9,img2,0.5,-1)
cv2.imshow("weighted",weight)
cv2.waitKey(0)
"""
#changes color dpending on the colors in the different images
"""subtract1 = cv2.subtract(img1,img2)
subtract2 = cv2.subtract(img2,img1)

cv2.waitKey(0)
cv2.imshow("smile_sub",subtract1)
cv2.imshow("pikachu_sub",subtract2)"""

#makes images bigger/smaller
"""resize = cv2.resize(img1,(500,500))

cv2.waitKey(0)
cv2.imshow("resized_img",resize)"""

#makes borders thicker
"""kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img2,kernel)
cv2.waitKey(0)
cv2.imshow("eroded",erosion)"""

#Gaussian Blur (Blurring img)
g = cv2.GaussianBlur(img2,(9,9),10)
cv2.imshow("Gaussian_Blur",g)



#Median Blur (Blurring img)
#Sharp edges are preserved but blurs everything else   
cv2.waitKey(0)
m = cv2.medianBlur(img2,9)
cv2.imshow("Median_Blur",m)

#Bilateral Blur (Blurring img)
cv2.waitKey(0)
b = cv2.bilateralFilter(img3,90,20,20)
cv2.imshow("Bilateral_Blur",b)

#Making Borders on image
cv2.waitKey(0)
cv2.destroyAllWindows()
borderedimg = cv2.copyMakeBorder(img2, 10,10,10,10, cv2.BORDER_CONSTANT, value = (255,0,0))
cv2.imshow("Bordered Pikachu", borderedimg)

#Reflective Border
cv2.waitKey(0)
cv2.destroyAllWindows()
reflectedimg = cv2.copyMakeBorder(img2, 300,300,300,300, cv2.BORDER_REFLECT, value = 1)
cv2.imshow("Reflected Pikachu", reflectedimg)


cv2.waitKey(0)
cv2.destroyAllWindows()






"""cv2.imshow("smile",img1)
cv2.imshow("pikachu",img2)"""

