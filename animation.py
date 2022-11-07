from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


class anim:
    def __init__(self,imgarray1,imgarray2,imgarray3):
        self.imgar1 = imgarray1
        self.imgar2 = imgarray2
        self.imgar3 = imgarray3


    def make_animation(self):
        figure, ax = plt.subplots()
        ani1 = animation.ArtistAnimation(figure, self.imgar1)
        ani2 = animation.ArtistAnimation(figure, self.imgar2)
        ani3 = animation.ArtistAnimation(figure, self.imgar3)
        plt.show()