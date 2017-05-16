import cv2
import glob
import os

files = glob.glob("*.jpg")

for file in files :
    img = cv2.imread(file,1)
    resized_image = cv2.resize(img, (100,100))
    cv2.imwrite("100x100_" + file, resized_image)


"""
img = cv2.imread("galaxy.jpg",1)

print(dir(img))
print(img)
print(img.shape)
print(img.ndim)


resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("galaxy_resized.jpg",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""