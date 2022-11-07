import cv2
import random

import numpy as np
from matplotlib import animation

import matplotlib.pyplot as plt


def randpixA(numpix):
    colv = 0
    col = 0
    a = []
    imgout = None
    ims = []
    fig, ax = plt.subplots(1, 3)
    for i in range(1, 41):
        img1 = cv2.imread(f"dataset/s{i}/1.pgm", 0)
        arr = make_arr(img1, numpix)
        m = 0
        for o in range(2, 11):
            img2 = cv2.imread(f"dataset/s{i}/{o}.pgm", 0)
            q = randpix(img2, arr)
            if q > m:
                m = q
                imgout = img2
        col += 1
        colv += 1
        t = False
        for o in range(1, 41):
            if o != i:
                for j in range(1, 11):
                    img3 = cv2.imread(f"dataset/s{o}/{j}.pgm", 0)
                    q = randpix(img3, arr)
                    if m < q:
                        colv -= 1
                        t = True
                        imgout = img3
                        break
                if t:
                    break
        ims.append([ax[0].imshow(img1, animated=True, cmap='gray'),
                    ax[1].imshow(imgout, animated=True, cmap='gray'),
                    ax[2].imshow(make_picture(img1,arr), animated=True, )])
        a.append(((colv / col) * 100))
    ani = animation.ArtistAnimation(fig, ims, blit=True, interval=1000, repeat=True)
    plt.show()
    return (colv / col) * 100


def make_arr(img1, num_pix):
    rows, cols = img1.shape
    arr = []
    for i in range(num_pix):
        rrows = random.randint(0, rows - 1)
        rcols = random.randint(0, cols - 1)
        arr.append((rrows, rcols, img1[rrows, rcols]))
    return arr


def randpix(img2, arr):
    for pix in arr:
        k1 = min(pix[2], int(img2[pix[0], pix[1]]))
        k2 = max(pix[2], int(img2[pix[0], pix[1]]))
        if k1 == 0:
            k1 += 1
        if k2 == 0:
            k2 += 1
        return (k1 / 255 * 100) / (k2 / 255 * 100) * 100


def make_picture(img1,arr):
    m = np.zeros(img1.shape)
    for i in arr:
        m[i[0], i[1]] = 255
    return m
