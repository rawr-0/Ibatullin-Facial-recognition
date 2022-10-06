import cv2
import random

import matplotlib.pyplot as plt


def randpixA(numpix):
    colv = 0
    col = 0
    a = []
    for i in range(1,41):
        img1 = cv2.imread(f"dataset/s{i}/1.pgm",0)
        arr = make_arr(img1,numpix)
        img2 = cv2.imread(f"dataset/s{i}/2.pgm",0)
        m = randpix(img2,arr)
        col+=1
        colv+=1
        t = False
        for o in range(1,41):
            if o != i:
                for j in range(1,11):
                    img3 = cv2.imread(f"dataset/s{o}/{j}.pgm",0)
                    q = randpix(img3,arr)
                    if m < q:
                        colv -= 1
                        t = True
                        break
                if t:
                    break
        #print((colv/col)*100)
        a.append(((colv/col)*100))
    #fig, ax = plt.subplots()
    #ax.plot(a,"red")
    #ax.set_xlabel("количество наборов")
    #ax.set_ylabel("точность")
    #plt.show()
    return (colv/col) *100


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