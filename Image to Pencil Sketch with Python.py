"""
Kamireddy RaviKaladhar Reddy
Data Science Internship at Let's Grow More
LGMVIP May 2022
Beginner Level Task - Image to Pencil sketch with python
"""
import cv2

# Using imread to read the original image
image = cv2.imread(r"C:\Users\ravik\Downloads\dog.jpg")
cv2.imshow("Dog", image)
cv2.waitKey(0)

# Reading black and white image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Dog", gray_image)
cv2.waitKey(0)

# Inverting the image- reversing the colours of the image
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

# Blurring the inverted image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred

# Creating Pencil Sketch
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

# Displaying the original image
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)
