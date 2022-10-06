import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def make_hist(img):
    st = cv.calcHist([img],[0],None,[256],[0,256],accumulate=False)
    st = cv.normalize(st,st,0,1,cv.NORM_MINMAX)
    return st

def HistA():
    colv = 0
    col = 0
    a = []
    for i in range(1,41):
        img1 = cv.imread(f"dataset/s{i}/1.pgm",0)
        img2 = cv.imread(f"dataset/s{i}/2.pgm",0)
        m = hist(img1,img2)
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
                        break
                if t:
                    break
        print((colv/col)*100)
        a.append(((colv/col)*100))
    fig, ax = plt.subplots()
    ax.plot(a, "red")
    ax.set_xlabel("количество наборов")
    ax.set_ylabel("точность")
    plt.show()
    print((colv/col) * 100)


def hist(img1,img2):
    hist_base = make_hist(img1)
    sum = 0.
    hist1 = make_hist(img2)
    out = cv.compareHist(hist_base,hist1,cv.HISTCMP_CORREL)
    sum += out
    return sum * 100