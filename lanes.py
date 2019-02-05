import cv2
import numpy as np
import matplotlib.pyplot as plt

# TODO: place in section comments

def simplify_img(lane_image):
    # change the image to gray for faster processing
    # reasoning: 1 value in each pixel array rather than 3 (RGB)
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

    # apply a blur to prevent detection of false edges
    # basically a 5 x 5 "kernel" is placed throughout image and the center pixel #
    # becomes the avg of the pixel values in the kernel
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # TODO: get the 0 value

    # use the Canny function to give an outline of the areas that have a gradient
    # aka it takes a derivative of two pixels and does this in all directions -- | /
    # basically a white line is made anywhere that exceeds the second gradient input
    # gradients between first gradient and second will only be white if it is connected to a pixel with gradient above ^^
    # everything else is blacked out
    canny = cv2.Canny(blur, 50, 150)
    return canny

def remove_all_outside_region_of_car_lane(image):
    # gets the bottom of the image (max # - just show image to see)
    height = image.shape[0]
    # array of triangles
    # each triangle array [point A, point B, point C]
    # the non-height numbers were just eye-balled using the plot
    polygons = np.array([
    [(200, height), (1100, height), (550, 250)]
    ])
    # blacken everything in image
    mask = np.zeros_like(image)
    # take black image and place a polygon inside, fill everything in the poly with color 255
    cv2.fillPoly(mask, polygons, 255)
    return mask

# reads the image & returns a multidimension array
# np.copy is just a clone of it so we don't edit the original
image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny = simplify_img(lane_image)

# plops a black image with a polygon
lane = remove_all_outside_region_of_car_lane(canny)
# shows the image when ran (opens in a new window)
# @waitKey sets the opened image to stay open until x is pressed
# cv2.imshow('result', canny)
# cv2.waitKey(0)

# shows the image with a graph
plt.imshow(lane)
plt.show()
