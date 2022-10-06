import quality
import methHist
import methRand
import methFourier
from matplotlib import pyplot as plt


# точность
# quality.qual()


# случайные пиксели
# s = 0
# a = []
# i = 1
# while i < 1101:
#     u = methRand.randpixA(i)
#     s = max(s,u)
#     a.append(u)
#     i+=100
#
# print(s)


# двумерное преобразование фурье
# s = 0
# a = []
# i = 100
# while i < 1101:
#     u = methFourier.FourierA(i)
#     print(u)
#     s = max(s,u)
#     a.append(u)
#     i+=100
#
# print(s)


# график
# fig, ax = plt.subplots()
# ax.plot(a, "red")
# ax.set_xlabel("количество наборов")
# ax.set_ylabel("точность")
# plt.show()


# гистогрма
methHist.HistA()
