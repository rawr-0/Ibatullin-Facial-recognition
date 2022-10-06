import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def fft(img):
    fft = np.fft.fft2(img)
    fft_shift = np.fft.fftshift(fft)
    absolute = (np.log(np.abs(fft_shift)+1)*10).astype(np.uint8)
    return absolute


def FourierA(size):
    colv = 0
    col = 0
    a = []
    for i in range(1, 41):
        img1 = cv.imread(f"dataset/s{i}/1.pgm", 0)
        img1 = cv.resize(img1,(size,size),interpolation=cv.INTER_AREA)
        img2 = cv.imread(f"dataset/s{i}/2.pgm", 0)
        img2 = cv.resize(img2, (size, size), interpolation=cv.INTER_AREA)
        #img1 = img1[31:82, 21:72]
        #img2 = img2[31:82, 21:72]
        m = Fourier(img1,img2)
        col += 1
        colv += 1
        t = False
        for o in range(1, 41):
            if o != i:
                for j in range(1, 11):
                    img3 = cv.imread(f"dataset/s{o}/{j}.pgm", 0)
                    img3 = cv.resize(img3, (size, size), interpolation=cv.INTER_AREA)
                    #img3 = img3[31:82, 21:72]
                    q = Fourier(img1, img3)
                    if m < q:
                        colv -= 1
                        t = True
                        break
                if t:
                    break
        a.append(((colv / col) * 100))
    return (colv/col)*100
    # fig, ax = plt.subplots()
    # ax.plot(a, "red")
    # ax.set_xlabel("количество наборов")
    # ax.set_ylabel("точность")
    # plt.show()


def Fourier(img1,img2):
    img1 = fft(img1)
    rows, cols = img1.shape
    img2 = fft(img2)
    sm = 0.
    for i in range(rows):
        for j in range(cols):
            k1 = min(int(img2[i][j]), int(img1[i][j]))
            k2 = max(int(img2[i][j]), int(img1[i][j]))
            if k1 == 0:
                k1 += 1
            if k2 == 0:
                k2 += 1
            sm += (k1 / 255 * 100) / (k2 / 255 * 100)
    mav = sm / (rows * cols)
    return mav * 100
