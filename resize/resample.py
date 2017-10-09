import cv2
import numpy as np
import math
from resize import interpolation as inter

class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
        originalImageRows, originalImagecols = image.shape
        print("Original Image Shape:  %s" % image.shape[0], image.shape[1])

        fxscale = float(fx)
        fyscale = float(fy)

        newImageRows = math.floor(originalImageRows*fyscale)
        newImageCols = math.floor(originalImagecols*fxscale)

        newImage = np.empty([newImageRows, newImageCols], dtype=np.uint8)
        print("Original Image Shape:  %s" % newImage.shape[0], newImage.shape[1])

        obj = inter.interpolation()

        for y in range(0, newImageRows):
            for x in range(0, newImageCols):
                dx = x / fxscale
                dy = y / fyscale
                rightX = math.ceil(dx)
                leftX = math.floor(dx)

                if math.ceil(dy) < originalImageRows:
                    dy = round(dy)
                else:
                    dy = math.floor(dy)

                if rightX < originalImagecols:
                    pix = obj.linear_interpolation((leftX,image[dy,leftX]), (rightX,image[dy,rightX]), dx)
                else:
                    pix = image[dy, leftX]

                newImage[y,x] = pix

        return newImage


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        originalImageRows, originalImageCols = image.shape
        print("Original Image Shape:  %s" % image.shape[0], image.shape[1])

        obj = inter.interpolation()

        fxscale = float(fx)
        fyscale = float(fy)

        # shape return tuple (0: row, 1: col)
        newImagerows = math.floor(originalImageRows * fyscale)
        newImagecols = math.floor(originalImageCols * fxscale)

        newImage = np.empty([newImagerows, newImagecols], dtype=np.uint8)
        print("Scaled New Image Shape:  %s" % newImage.shape[0],newImage.shape[1])

        for y in range(0, newImagerows):
            for x in range(0, newImagecols):
                dx = x / fxscale
                dy = y / fyscale

                leftX = math.floor(dx); rightX = math.ceil(dx)   #leftX --dx-- rightX
                topY = math.floor(dy); bottomY = math.ceil(dy)   #topY
                                                                 #|
                                                                 #dy
                                                                 #|
                                                                 #bottomY
                if rightX >= originalImageCols:
                    rightX = originalImageCols-1
                if bottomY >= originalImageRows:
                    bottomY = originalImageRows-1
                                                  #          _C O L S__
                                                  #           leftX  dX     rightX
                q11 = image[topY,leftX]           #R    topY| q11    r1    q21
                q12 = image[bottomY,leftX]        #O      dY|        P
                q21 = image[topY,rightX]          #W        |
                q22 = image[bottomY,rightX]       #S bottomY| q12    r2    q22

                newImage[y,x] = obj.bilinear_interpolation((leftX,q11,q12),(rightX,q21,q22), bottomY, topY, (dx,dy))

        return newImage

