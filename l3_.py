import cv2

img1 = cv2.imread("pikachu.png", 0)

img3 = cv2.imread("pikachu.png", 1)

#Method 1 grayscale
cv2.imshow("Pikachu gray", img1)

"""#Method 2 grayscale
img2 = cv2.imread("pikachu.png", cv2.COLOR_BGR2GRAY)
cv2.imshow("pikachu gray 2", img2)"""

#Rotation
(rows,cols) = img3.shape[:2]
#                                        end values  |rotation|scales image 
rotationmatrix = cv2.getRotationMatrix2D((cols/2, rows/2),90, 0.5)
finalimg = cv2.warpAffine(img3, rotationmatrix, (cols,rows))

cv2.imshow("Rotated pikachu", finalimg)

#Color mode change RGB ---> HSV

hsvimg = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Pikachu", hsvimg)

#Edge detection
detectimglow = cv2.Canny(img3, 2,2)
cv2.imshow("Decting edges Pikachu", detectimglow)

detectimghigh = cv2.Canny(img3, 1000,1000)
cv2.imshow("Dectingg edges Pikachu", detectimghigh)


cv2.waitKey(0)
cv2.destroyAllWindows()