# Based on https://docs.opencv.org/master/dc/dbb/tutorial_py_calibration.html

import argparse
import os
import pickle
import sys

import numpy as np
import cv2 as cv

parser = argparse.ArgumentParser()
parser.add_argument('--parameter_path')
parser.add_argument('--image_path')
parser.add_argument('--output_path')
args = parser.parse_args(sys.argv[1:])

with open(args.parameter_path, 'rb') as f:
  _, mtx, dist, rvecs, tvecs = pickle.load(f)

image = cv.imread(args.image_path)
h,  w = image.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
dst = cv.undistort(image, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite(args.output_path, dst)