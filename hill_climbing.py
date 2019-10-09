import func_file, static_data

import numpy as np


def hill_climbing(name_function, mux, muy, sigma, size, iterat):
    list_points = []
    generated_x = np.random.normal(mux, sigma, size)
    generated_y = np.random.normal(muy, sigma, size)
    tmp = func_file.return_value_function([mux, muy], name_function)
    for i, j in zip(generated_x, generated_y):
        min = func_file.return_value_function([i, j], name_function)
        list_points.append([i, j, min])
        if min < tmp:
            tmp = min
            cord_X = i
            cord_Y = j

    print("Iteration n.: " + str(iterat))
    print("X: " + str(cord_X))
    print("Y: " + str(cord_Y))
    print("VALUE: " + str(tmp))


    if iterat == 1:
        return [cord_X, cord_Y, tmp]
    else:
        return hill_climbing(name_function, cord_X, cord_Y, sigma, size, iterat - 1)
