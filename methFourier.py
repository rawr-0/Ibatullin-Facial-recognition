import cmath
import math

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation


def fft(img):
    fft = np.fft.fft2(img)
    fft_shift = np.fft.fftshift(fft)
    absolute = (np.log(np.abs(fft_shift)+1)*10).astype(np.float)
    return fft_shift


def FourierA(size):
    colv = 0
    col = 0
    a = []
    imgout = None
    ims = []
    ims4 = []
    fig, ax = plt.subplots(3, 2)
    fig.delaxes(ax[2][1])
    ax[0][0].title.set_text("эталон")
    ax[0][1].title.set_text("ответ программы")
    ax[1][0].title.set_text("преобразование Фурье эталона")
    ax[1][1].title.set_text("преобразование Фурье  ответа")
    ax[2][0].title.set_text("график точности")
    ax[2][0].set_xlabel("количество тестов")
    ax[2][0].set_ylabel("точность %")

    for i in range(1, 41):
        img1 = cv.imread(f"dataset/s{i}/1.pgm", 0)
        #img1 = cv.resize(img1,(size,size),interpolation=cv.INTER_AREA)
        m = 0
        for o in range(2,11):
            img2 = cv.imread(f"dataset/s{i}/{o}.pgm", 0)
            #img2 = cv.resize(img2, (size, size), interpolation=cv.INTER_AREA)
            q = Fourier(img1, img2)
            if q > m:
                m = q
                imgout = img2
        #img1 = img1[31:82, 21:72]
        #img2 = img2[31:82, 21:72]
        col += 1
        colv += 1
        t = False
        for o in range(1, 41):
            if o != i:
                for j in range(1, 11):
                    img3 = cv.imread(f"dataset/s{o}/{j}.pgm", 0)
                    #img3 = cv.resize(img3, (size, size), interpolation=cv.INTER_AREA)
                    #img3 = img3[31:82, 21:72]
                    q = Fourier(img1, img3)
                    if m < q:
                        colv -= 1
                        t = True
                        imgout = img3
                        break
                if t:
                    break
        ims.append([ax[0][0].imshow(img1, animated=True, cmap='gray'),
                    ax[0][1].imshow(imgout, animated=True, cmap='gray'),
                    ax[1][0].imshow((np.log(np.abs(fft(img1)+1)*10).astype(np.float)), animated=True, cmap='gray'),
                    ax[1][1].imshow((np.log(np.abs(fft(imgout)+1)*10).astype(np.float)), animated=True, cmap='gray')])
        a.append((colv / col) * 100)
        ims4.append(ax[2][0].plot(a, 'r'))
    ani = ArtistAnimation(fig, ims, blit=True, interval=1000, repeat=True)
    #ani2 = ArtistAnimation(fig, ims4, blit=True , interval=1000, repeat=True)
    plt.show()
    plt.close()
    return (colv/col)*100


def Fourier(img1, img2):
    img1 = fft(img1)
    rows, cols = img1.shape
    img2 = fft(img2)
    sm = 0.
    for i in range(int(rows/3),int(rows-rows/3)):
        for j in range(int(cols/3),int(cols-cols/3)):
            sm += pow(img2[i][j].real-img1[i][j].real, 2)+pow(img2[i][j].imag-img1[i][j].imag, 2)
    mav = (rows * cols)/sm
    return mav * 100
