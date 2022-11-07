import cv2
import numpy as np
import random
from matplotlib import animation
from matplotlib import pyplot as plt

def fft(img):
    fft = np.fft.fft2(img)
    fft_shift = np.fft.fftshift(fft)
    absolute = (np.log(np.abs(fft_shift)+1)*15).astype(np.uint8)
    return absolute

def make_arr(img1,num_pix):
    rows, cols = img1.shape
    arr = []
    for i in range(num_pix):
        rrows = random.randint(0, rows - 1)
        rcols = random.randint(0, cols - 1)
        arr.append((rrows, rcols, img1[rrows, rcols]))
    return arr


def randpix(img2,arr):
    for pix in arr:
        k1 = min(pix[2], int(img2[pix[0], pix[1]]))
        k2 = max(pix[2], int(img2[pix[0], pix[1]]))
        if k1 == 0:
           k1 += 1
        if k2 == 0:
            k2 += 1
        return (k1 / 255 * 100) / (k2 / 255 * 100) * 100


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


def make_hist(img):
    st = cv2.calcHist([img],[0],None,[256],[0,256],accumulate=False)
    st = cv2.normalize(st,st,0,1,cv2.NORM_MINMAX)
    return st


def hist(img1,img2):
    hist_base = make_hist(img1)
    sum = 0.
    hist1 = make_hist(img2)
    out = cv2.compareHist(hist_base,hist1,cv2.HISTCMP_CORREL)
    sum += out
    return sum * 100

def vote(numpix):
    colv = 0
    col = 0
    imgout1 = None; imgout2 = None; imgout3 = None
    a = []
    ims1 = []
    fig, ax = plt.subplots(1, 4)
    for i in range(1,41):
        m1 = 0
        m2 = 0
        m3 = 0
        img1 = cv2.imread(f"dataset/s{i}/1.pgm",0)
        arr = make_arr(img1,numpix)
        for o in range(2,11):
            img2 = cv2.imread(f"dataset/s{i}/2.pgm",0)
            q1 = randpix(img2, arr)
            q2 = Fourier(img1, img2)
            q3 = hist(img1, img2)
            if m1 < q1 and m2 < q2 and m3 < q3 or m1 > q1 and m2 < q2 and m3 < q3 or m1 < q1 and m2 > q2 and m3 < q3 or m1 < q1 and m2 < q2 and m3 > q3:
                m1 = q1
                m2 = q2
                m3 = q3
                imgout1 = img2
                imgout2 = img2
                imgout3 = img2
        col+=1
        colv+=1
        t = False
        for o in range(1,41):
            if o != i:
                for j in range(1,11):
                    img3 = cv2.imread(f"dataset/s{o}/{j}.pgm",0)
                    q1 = randpix(img3,arr)
                    q2 = Fourier(img1, img3)
                    q3 = hist(img1, img3)
                    if m1 < q1:
                        imgout1 = img3
                    if m2 < q2:
                        imgout2 = img3
                    if m3 < q3:
                        imgout3 = img3
                    if m1 < q1 and m2 < q2 and m3 < q3 or m1 > q1 and m2 < q2 and m3 < q3 or m1 < q1 and m2 > q2 and m3 < q3 or m1 < q1 and m2 < q2 and m3 > q3:
                        colv -= 1
                        t = True
                        break
                if t:
                    break
        ims1.append([ax[0].imshow(img1, animated=True, cmap='gray'),
                    ax[1].imshow(imgout1, animated=True, cmap='gray'),
                    ax[2].imshow(imgout2, animated=True, cmap='gray'),
                    ax[3].imshow(imgout3, animated=True, cmap='gray')])
        #print((colv/col)*100)
        a.append(((colv/col)*100))
    ani = animation.ArtistAnimation(fig, ims1, blit=True, interval=1000, repeat=True)
    plt.show()
    return (colv/col) *100


