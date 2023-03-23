
import glob
import numpy as np
import imutils
import cv2


# image_paths=glob.glob('/home/nam/바탕화면/CameraCalibration/results/*.jpg')
images = []

# path1 = '/home/nam/바탕화면/CameraCalibration/sample_data/basement_0322/back/1.jpg'
# path2 = '/home/nam/바탕화면/CameraCalibration/sample_data/basement_0322/left/1.jpg'
# path3 = '/home/nam/바탕화면/CameraCalibration/sample_data/basement_0322/right/1.jpg'
# path4 = '/home/nam/바탕화면/CameraCalibration/sample_data/basement_0322/front/1.jpg'
path1 = '/home/nam/바탕화면/CameraCalibration/results/back.jpg'
path2 = '/home/nam/바탕화면/CameraCalibration/results/front.jpg'
path3 = '/home/nam/바탕화면/CameraCalibration/results/left.jpg'
path4 = '/home/nam/바탕화면/CameraCalibration/results/right.jpg'


image_paths = [path3, path4]

for image in image_paths:
    img = cv2.imread(image)
    images.append(img)
    cv2.imshow('image', img)
    cv2.waitKey(0)

imageStitcher = cv2.Stitcher_create()
error, stitched_img = imageStitcher.stitch(images)
print(stitched_img)


if not error:
    print('here')
    cv2.imwrite('stitched_image.png', stitched_img)
    cv2.namedWindow(str('delta'), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
    cv2.imshow('delta', stitched_img)
    cv2.waitKey(0)
    
