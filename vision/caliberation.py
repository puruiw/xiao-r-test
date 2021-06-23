# Based on https://docs.opencv.org/master/dc/dbb/tutorial_py_calibration.html

import argparse
import os
import pickle
import sys

import numpy as np
import cv2 as cv
import glob

parser = argparse.ArgumentParser()
parser.add_argument('--image_directory')
parser.add_argument('--output_path')
parser.add_argument('--capture', action='store_true')
args = parser.parse_args(sys.argv[1:])

BOARD_SIZE = (7, 7)


def capture_one():
  """Capture one image from the first camera.

  We have to open and release the camera every time. Otherwise it may return
  buffered frames.
  """
  camera = cv.VideoCapture(0)
  if not camera.isOpened():
    raise Exception('Cannot open video device.')
  ret, image = camera.read()
  if not ret:
    camera.release()
    raise Exception('Cannot read next frame.')
  camera.release()
  return image


def interactive_capture(directory, n):
  for i in range(n):
    success = False
    while not success:
      _ = input(f'Capturing {i+1}, hit Enter.')
      image = capture_one()
      gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
      success, corners = cv.findChessboardCorners(gray, BOARD_SIZE, None)
    cv.imwrite(os.path.join(directory, '%03d.jpg' % i), image)
  

if args.capture:
  interactive_capture(args.image_directory, 15)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((np.prod(BOARD_SIZE),3), np.float32)
objp[:,:2] = np.mgrid[0:BOARD_SIZE[0],0:BOARD_SIZE[1]].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob(os.path.join(args.image_directory, '*.jpg'))
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, BOARD_SIZE, None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
with open(args.output_path, 'wb') as f:
  pickle.dump([ret, mtx, dist, rvecs, tvecs], f)
print([ret, mtx, dist, rvecs, tvecs])