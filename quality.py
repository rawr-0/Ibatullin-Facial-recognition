import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def fft(img):
    fft = np.fft.fft2(img)
    fft_shift = np.fft.fftshift(fft)
    absolute = (np.log(np.abs(fft_shift)+1)*15).astype(np.uint8)
    return absolute


def qual():
    ref = cv.imread("dataset/s1/1.pgm",0)
    ref = ref[40:95,17:75]
    plt.imshow(ref,cmap='gray')
    plt.show()
    ref = fft(ref)
    mav = 0
    for i in range(1,41):
        for j in range(1,11):
            img = cv.imread(f"dataset/s{i}/{j}.pgm",0)
            img = img[40:95,17:75]
            img = fft(img)
            sm = 0.
            for i1 in range(95-40):
                for j1 in range(75-17):
                    k1 = min(int(ref[i1][j1]), int(img[i1][j1]))
                    k2 = max(int(ref[i1][j1]), int(img[i1][j1]))
                    if k1 == 0:
                        k1 += 1
                    if k2 == 0:
                        k2 += 1
                    sm += ((k1 / 255 * 100) / (k2 / 255 * 100))/((95-40)*(75-17))
            mav += sm
    print(f"quality = {mav/4}")