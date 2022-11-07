import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import animation
matplotlib.use('TkAgg')


def make_hist(img):
    st = cv.calcHist([img],[0],None,[256],[0,256],accumulate=False)
    #st = cv.normalize(st,st,0,1,cv.NORM_MINMAX)
    return st

def HistA():
    colv = 0
    col = 0
    a = []
    imgout = None
    ims = []
    ims2 = []
    ims3 = []
    fig, ax = plt.subplots(2, 2)
    for i in range(1,41):
        m = 0
        img1 = cv.imread(f"dataset/s{i}/1.pgm",0)
        for o in range(2,11):
            img2 = cv.imread(f"dataset/s{i}/2.pgm",0)
            q = hist(img1,img2)
            if q > m:
                m = q
                imgout = img2
        col+=1
        colv+=1
        t = False
        for o in range(1,41):
            if o != i:
                for j in range(1,11):
                    img3 = cv.imread(f"dataset/s{o}/{j}.pgm",0)
                    q = hist(img1,img3)
                    if m < q:
                        colv -= 1
                        t = True
                        imgout = img3
                        break
                if t:
                    break
        ims.append([ax[0][0].imshow(img1, animated=True, cmap='gray'),
                    ax[0][1].imshow(imgout, animated=True, cmap='gray'),
                    ])
        ims2.append(ax[1][0].plot(make_hist(img1)))
        ims3.append(ax[1][1].plot(make_hist(imgout)))
        a.append(((colv / col) * 100))
    ani = animation.ArtistAnimation(fig, ims, blit=True, interval=1000, repeat=True)
    ani2 = animation.ArtistAnimation(fig, ims2, blit=True, interval=1000, repeat=True)
    ani3 = animation.ArtistAnimation(fig, ims3, blit=True, interval=1000, repeat=True)
    plt.show()
    return (colv/col) * 100
def hist(img1,img2):
    hist_base = make_hist(img1)
    sum = 0.
    hist1 = make_hist(img2)
    out = cv.compareHist(hist_base,hist1,cv.HISTCMP_CORREL)
    sum += out
    return sum * 100