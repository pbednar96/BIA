import math
import numpy as np
import func_file
import random


def simulated_annealing(name_function, mux, muy, sigma, size, iterat, temperature_0):
    temperature_decrease = lambda temperature: temperature * 0.99
    temperature_min = 0.1
    list_points = []
    generated_x = np.random.normal(mux, sigma, size)
    generated_y = np.random.normal(muy, sigma, size)
    tmp = func_file.return_value_function([mux, muy], name_function)
    cord_X = generated_x[0]
    cord_Y = generated_y[0]
    if temperature_0 > temperature_min:
        for i, j in zip(generated_x, generated_y):
            min = func_file.return_value_function([i, j], name_function)
            list_points.append([i, j, min])
            if min < tmp:
                tmp = min
                cord_X = i
                cord_Y = j
            else:
                r = random.uniform(0, 1)
                if r > (math.exp(tmp / temperature_0)) - 1:
                    tmp = min
                    cord_X = i
                    cord_Y = j
            temperature_0 = temperature_decrease(temperature_0)

    print("Iteration n.: " + str(iterat))
    print("X: " + str(cord_X))
    print("Y: " + str(cord_Y))
    print("VALUE: " + str(tmp))
    print("")


    if iterat == 1:
        return [cord_X, cord_Y, tmp]
    else:
        return simulated_annealing(name_function, cord_X, cord_Y, sigma, size, iterat - 1, temperature_0)
