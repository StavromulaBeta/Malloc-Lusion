import cv2
import numpy as np

image = np.zeros((1500,1500,1), np.uint8)



arch1 = [0, 0.72, -1.01, -1.08, 1.08, 1.11, 0.32, -1.19, -1.11, -1.14, 1.08, 1.00, 0, 0.8, -1.69, 1.01]
arch2 = [0] * 16

toothx = 50
toothy = 100
spacing = 50

a1y = int(300 - toothy/2)
a2y = int(1200 - toothy/2)

x = 100
for tooth in arch1:
    offset = tooth * 100
    print(a1y + offset)
    cv2.rectangle(image, (x, int(a1y + offset)), (x + toothx, int(a1y + offset) + toothy), 255, -1)
    x = x + toothx + spacing


x = 100
for tooth in arch2:
    offset = tooth * 100
    print(a1y + offset)
    cv2.rectangle(image, (x, int(a2y + offset)), (x + toothx, int(a2y + offset) + toothy), 255, -1)
    x = x + toothx + spacing



cv2.imwrite('helloworld.png', image)

cv2.imshow('Image', image)
cv2.waitKey(0) # Waits indefinitely until a key is pressed.
cv2.destroyAllWindows() # Closes all windows opened by program.
