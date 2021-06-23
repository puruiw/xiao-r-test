import sys

import cv2 as cv

input_path = sys.argv[1]
output_path = sys.argv[2]

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

img = cv.imread(input_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, corners = cv.findChessboardCorners(gray, (7, 7))
if ret == True:

  # Not improving precision for images from the XiaoR camera.
  corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
  
  print(f"corners: {corners}")
  print(f"corners2: {corners2}")
  cv.drawChessboardCorners(img, (7, 7), corners2, ret)
  cv.imwrite(output_path, img)