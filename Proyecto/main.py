import cv2

img = cv2.imread("images/conejitos.jpg")
#print(img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray.jpg", gray)
