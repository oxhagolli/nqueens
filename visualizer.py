"""
    N-Queens configuration visualizer

    Author: Orens Xhagolli (oxx6096@cs.rit.edu)
    Dec. 4th, 2018
"""
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt

queens = 64


def draw(config):
    """
    Visualizes matrix of queens
    :param config: binary matrix of queens
    :return:
    """
    image = Image.open("queen.png").resize((queens - 2, queens-2), Image.ANTIALIAS)
    for row, i in enumerate(config):
        for col, j in enumerate(i):
            if j is 1:
                plt.imshow(image, extent=(col*queens, col*queens + queens -2, row*queens, row*queens + queens - 2))
    draw_grid(len(config))
    plt.show()


def draw_grid(size, color="blue"):
    for i in range(1, size):
        plt.plot([i*queens, i*queens], [0, size*queens], color=color)
        plt.plot([0, size*queens], [i*queens, i*queens], color=color)


draw([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
