import cv2
from numpy import random


def add_noise(img):
    # Getting the dimensions of the image
    if(len(img.shape) == 2):
        row, col = img.shape
    else:
        row, col, ch = img.shape
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to white
        img[y_coord][x_coord] = 255

    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to black
        img[y_coord][x_coord] = 0

    return img
def gaussian_blur(img, value):
    if(value > 0):
        value = convertValidValue(value)
        img = cv2.GaussianBlur(img, (value, value), 0)
    return img
def box_blur(img, value):
    if (value > 0):
        value = convertValidValue(value)
        img = cv2.boxFilter(img, -1, (value, value))
    return img

def median_blur(img, value):
    if (value > 0):
        value = convertValidValue(value)
        img = cv2.medianBlur(img, value)
    return img
def convertValidValue(value):
    if value % 2 == 0:
        value += 1
    return value
