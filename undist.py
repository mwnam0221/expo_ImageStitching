import cv2
import os
import numpy as np
from ExtrinsicCalibration import ExCalibrator
from IntrinsicCalibration import InCalibrator, CalibMode
from SurroundBirdEyeView import BevGenerator
import glob

def runInCalib_1():
    print("Intrinsic Calibration ......")
    calibrator = InCalibrator('fisheye')                # 初始化内参标定器
    PATH = './IntrinsicCalibration/data/'
    images = os.listdir(PATH)
    for img in images:
        print(PATH + img)
        raw_frame = cv2.imread(PATH + img)
        result = calibrator(raw_frame)                  # 每次读入一张原始图片 更新标定结果

    print("Camera Matrix is : {}".format(result.camera_mat.tolist()))
    print("Distortion Coefficient is : {}".format(result.dist_coeff.tolist()))
    print("Reprojection Error is : {}".format(np.mean(result.reproj_err)))


    img_path = glob.glob('./sample_data/*.jpg')
    print(img_path)
    for i, path in enumerate(img_path):
        name = path.split('/')[-1].split('.')[0]
        print(name)
        raw_frame = cv2.imread(path)
        # cv2.imshow("Raw Image", raw_frame)
        undist_img = calibrator.undistort(raw_frame)        # 使用undistort方法得到去畸变图像
        cv2.imshow(f"Undistorted Image_{name}", undist_img)
        cv2.imwrite(f'./results/{name}.jpg', undist_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

runInCalib_1()