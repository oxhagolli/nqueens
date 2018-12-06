"""
    N-Queens puzzle solver

    Author: Orens Xhagolli
    Dec 4th, 2018
"""

from visualizer import draw

import numpy as np


def empty_config(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def solve(config):
    if sum(sum(np.array(config))) == len(config) and is_valid(config):
        return config
    else:
        children = generate_children(config)
        soln = None
        for child in children:
            if is_valid(child):
                current = solve(child)
                if current is not None:
                    soln = current
        return soln


def generate_children(config):
    col = sum(sum(np.array(config)))
    result = []
    for i in range(len(config)):
        copy = [x[:] for x in config]
        copy[i][col] = 1
        result.append(copy)
    return result


def is_valid(config):
    size = len(config)
    queens = sum(sum(np.array(config)))
    if queens == 0:
        return True
    for i in range(size):
        for j in range(size):
            if config[i][j] == 1:
                # Generate matrix
                copy = empty_config(size)
                for k in range(size):
                    copy[i][k] = 1
                    copy[k][j] = 1
                    if i - k >= 0 and j - k >= 0:
                        copy[i-k][j-k] = 1
                    if i + k < size and j - k >= 0:
                        copy[i+k][j-k] = 1
                    if i - k >= 0 and j + k < size:
                        copy[i-k][j+k] = 1
                    if i + k < size and j + k < size:
                        copy[i+k][j+k] = 1
                A = np.array(copy)
                x = np.array(config)
                b = np.logical_and(A, x)
                if sum(sum(b)) > 1:
                    return False
    return True


c = empty_config(4)
draw(c)
soln = solve(c)
draw(soln)
