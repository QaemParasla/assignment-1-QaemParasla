import numpy as np
import math
import cv2

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256
        for row in range(0, image.shape[0]):
            for col in range(0, image.shape[1]):
                pixel = image[row, col]
                hist[pixel] += 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = 128
        mu1 = 0
        mu2 = 0
        rsum = sum(hist[0:threshold])
        ssum = sum(hist[threshold:256])

        while True:
            for x in range(0, threshold):
                mu1 += ((hist[x] / rsum) * (x + 1))
            # print("mu1 %s" % mu1)

            for x in range(threshold, 256):
                mu2 += ((hist[x] / ssum) * (x + 1))
            #print("mu2 %s" % mu2)

            newThreshold = math.ceil((mu1 + mu2) / 2.0)

            if threshold == newThreshold:
                break
            else:
                threshold = newThreshold
                rsum = sum(hist[0:threshold])
                ssum = sum(hist[threshold:256])
                mu1 = 0
                mu2 = 0

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        threshold = self.find_optimal_threshold(self.compute_histogram(image))
        bin_img = image.copy()
        cv2.imshow('image', bin_img)
        cv2.waitKey(0)
        for row in range(0, bin_img.shape[0]):
            for col in range(0, bin_img.shape[1]):
                if bin_img[row, col] < threshold:
                    bin_img[row, col] = 255
                elif bin_img[row, col] >= threshold:
                    bin_img[row, col] = 0

        return bin_img


