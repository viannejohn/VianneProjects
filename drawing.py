import cv2

image_path='Arsenal1.jfif'

image=cv2.imread(image_path)
#image = cv2.resize(image, (420,300))

text = "ARSENAL"
coordinates = (800,100)
font = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
color = (255,0,0)
thickness = 2

color = (255,0,0)
thickness = 2
centre_coordinates = (800,500)
#end_point = (500,500)
radius = 100
image = cv2.circle(image, centre_coordinates, radius, color, thickness)

color = (255,0,255)
thickness = 2
center_coordinates = (500,500)
axeslength = (100,50)
angle = 30
startangle = 0
endangle = 360
image = cv2.ellipse(image, center_coordinates, axeslength, angle, startangle, endangle, color, thickness)

color = (255,0,0)
thickness = 2
start_point = (100,100)
end_point = (200,200)
image = cv2.rectangle(image, start_point, end_point, color, thickness)

image = cv2.putText(image, text, coordinates, font, fontScale, color, thickness)
cv2.imshow('Original Image', image)
#cv2.imshow('Resized Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
