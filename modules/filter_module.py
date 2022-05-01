import cv2

class BlurFunction():
    gaussianValue = 0
    boxValue = 0
    medianValue = 0

    def __init__(self):
        print('')

    def gaussian(self):
        new_value = self.gaussianValue
        if self.gaussianValue % 2 == 0:
            new_value = self.gaussianValue + 1
        self.new_image = cv2.GaussianBlur(self.new_image, (new_value, new_value), 0)



