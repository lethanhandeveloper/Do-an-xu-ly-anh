import cv2

def rotateImage(main):
    rows, cols, steps = main.new_image.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), main.rotateValue, 1)  # thay đổi chiều của ảnh
    main.new_image = cv2.warpAffine(main.new_image, M, (cols, rows))