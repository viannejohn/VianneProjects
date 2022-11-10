import cv2

image_path='Arsenal_FC.png.png'

image=cv2.imread(image_path)
image = cv2.resize(image, (420,300))
#cv2.imshow('Sample Image', image)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

#directory=r'C:\Users\user\PycharmProjects\VianneProjects'

#filename='Arsenal.png'
#cv2.imwrite(filename, image)
#print('Image was successfully saved')

#print(image.shape)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', image)
cv2.imshow('Gray Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()