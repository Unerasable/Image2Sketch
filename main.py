import cv2
image_input = input("The location of the image: ")
image = cv2.imread(image_input)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch of the Image", pencil_sketch)
cv2.waitKey(0)