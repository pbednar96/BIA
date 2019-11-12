#PYTHON IMPORT
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#MY IMPORT
import show_3D_graph, static_data


def ackley(input_data):
    # ok
    a = 20
    b = 0.2
    c = 2 * np.pi
    sum1 = np.array(input_data)
    sum1 = np.sum(sum1 ** 2)

    sum2 = np.array(input_data)
    sum2 = np.cos(c * sum2)
    sum2 = np.sum(sum2)

    term1 = - a * np.exp(-b * math.sqrt((1 / len(input_data)) * sum1 ** 2))
    term2 = - np.exp((1 / len(input_data)) * sum2)

    return term1 + term2 + a + np.exp(1)


def levy(input_data):
    # also bad
    sum1 = 0
    for i in range(len(input_data)):
        w = 1 + ((input_data[i] - 1) / 4)
        wd = 1 + ((input_data[len(input_data) - 1] - 1) / 4)
        sum1 = sum1 + ((((w - 1) ** 2) * (1 + (10 * math.sin(math.pi * w + 1))**2)) + (((wd - 1) ** 2) * (
                1 + math.sin(2 * math.pi * wd) ** 2)))
    return (math.sin(math.pi * (1 + (input_data[0] - 1) / 4)) ** 2) + sum1


def griewank(input_data):
    # ok
    sum1 = [(item ** 2) / 4000 for item in input_data]
    sum2 = 1
    for i, item in enumerate(input_data):
        sum2 = sum2 * math.cos(item / ((i + 1) ** .5))
    return sum(sum1) - sum2 + 1


def rastrigin(input_data):
    # good job!!
    sum = 0
    for item in input_data:
        sum = sum + (item ** 2 + - 10 * math.cos(2 * np.pi * item))
    return 10 * len(input_data) + sum


def schwefel(input_data):
    # OK
    sum1 = 0
    for item in input_data:
        sum1 = sum1 + item * math.sin((abs(item)) ** .5)
    return 418.9829 * len(input_data) - sum1


def zakharov(input_data):
    # bad
    sum1 = [item ** 2 for item in input_data]
    sum2 = [(0.5 * i + 1 * item) ** 2 for i, item in enumerate(input_data)]
    sum3 = [(0.5 * i + 1 * item) ** 4 for i, item in enumerate(input_data)]
    result = sum(sum1) + sum(sum2) + sum(sum3)
    return result


def sphere(input_data):
    # EZ
    sum1 = np.array(input_data)
    return np.sum(sum1 ** 2)


def michalewicz(input_data):
    # bad
    m = 10
    sum1 = 0
    for i, item in enumerate(input_data):
        sum1 = sum1 + ((math.sin(item)) * (((math.sin((i + 1) * item ** 2)) / math.pi) ** (2 * m)))
    return -(sum1)

def return_value_function(input_data,name_function):
    if name_function == "ackley":
        return ackley(input_data)
    elif name_function == "levy":
        return levy(input_data)
    elif name_function == "griewank":
        return griewank(input_data)
    elif name_function == "schwefel":
        return schwefel(input_data)
    elif name_function == "zakharov":
        return zakharov(input_data)
    elif name_function == "sphere":
        return sphere(input_data)
    elif name_function == "michalewicz":
        return michalewicz(input_data)
    elif name_function == "rastrigin":
        return rastrigin(input_data)
    else:
        return 0


#show_3D_graph.show_graph("sphere")
