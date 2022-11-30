import methHist
import methRand
import methFourier
import hist2
import fourier
import vote
from matplotlib import pyplot as plt


#случайные пиксели
# s = 0
# a = []
# i = 1
# while i < 1101:
print(methRand.randpixA(400))
#     # s = max(s,u)
#     # a.append(u)
#     # i+=100
#
# график
# fig, ax = plt.subplots()
# ax.plot(a, "red")
# ax.set_xlabel("количество наборов")
# ax.set_ylabel("точность")
# plt.show()

print(methHist.HistA())
##двумерное преобразование фурье
# s = 0
# a = []
# i = 100
# while i < 1101:
u = methFourier.FourierA(112)
print(u)
#     s = max(s,u)
#     a.append(u)
#     i+=100
#
# print(s)

# гистограмма

print(vote.vote(200))
