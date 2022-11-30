import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import ArtistAnimation


def make_hist(img):
    st = cv.calcHist([img],[0],None,[32],[0,256],accumulate=True)
    st = cv.normalize(st,st,0,1,cv.NORM_MINMAX)
    return st

def HistA():
    colv = 0
    col = 0
    a = []
    imgout = None
    ims = []
    ims2 = []
    ims3 = []
    ims4 = []
    fig, ax = plt.subplots(3, 2)
    fig.delaxes(ax[2][1])
    ax[0][0].title.set_text("эталон")
    ax[0][1].title.set_text("ответ программы")
    ax[1][0].title.set_text("гистограмма эталона")
    ax[1][1].title.set_text("гистограмма ответа")
    ax[2][0].title.set_text("график точности")
    ax[1][0].set_xlabel("столбцы")
    ax[1][1].set_xlabel("столбцы")
    ax[2][0].set_xlabel("количество тестов")
    ax[2][0].set_ylabel("точность %")

    for i in range(1,41):
        m = 0
        img1 = cv.imread(f"dataset/s{i}/1.pgm",0)
        #ref = cv.imread(f"dataset/s{i}/2.pgm",0)
        for o in range(2, 11):
            img2 = cv.imread(f"dataset/s{i}/{o}.pgm", 0)
            q1 = hist(img1,img2)
            #q2 = hist(ref,img2)
            #q1 = max(q1,q2)
            if q1 > m:
                m = q1
                imgout = img2
        col+=1
        colv+=1
        t = False
        for o in range(1,41):
            if o != i:
                for j in range(1,11):
                    img3 = cv.imread(f"dataset/s{o}/{j}.pgm", 0)
                    q1 = hist(img1, img3)
                    #q2 = hist(ref, img3)
                    #q1 = max(q1, q2)
                    if m < q1:
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
        a.append((colv / col) * 100)
        ims4.append(ax[2][0].plot(a,'r'))
    ani = ArtistAnimation(fig, ims, blit=True, interval=1000, repeat=True)
    ani2 = ArtistAnimation(fig, ims2, blit=True, interval=1000, repeat=True)
    ani3 = ArtistAnimation(fig, ims3, blit=True, interval=1000, repeat=True)
    #ani4 = ArtistAnimation(fig, ims4, blit=True, interval=1000, repeat=True)
    plt.show()
    return (colv/col) * 100


def hist(img1,img2):
    hist_base = make_hist(img1)
    sum = 0.
    hist1 = make_hist(img2)
    out = cv.compareHist(hist_base,hist1,cv.HISTCMP_CORREL)
    sum += out
    return sum * 100