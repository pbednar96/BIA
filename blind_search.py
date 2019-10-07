import numpy as np
import random
import static_data, func_file


def blind_search(name_function, size_random_search):
    point_list = []
    generated_data_x = [
        random.uniform(static_data.get_min_range(name_function), static_data.get_max_range(name_function))
        for _ in range(size_random_search)]

    generated_data_y = [
        random.uniform(static_data.get_min_range(name_function), static_data.get_max_range(name_function))
        for _ in range(size_random_search)]
    tmp = func_file.return_value_function([generated_data_x[0], generated_data_y[0]], name_function)
    cord_X = generated_data_x[0]
    cord_Y = generated_data_y[0]
    for i, j in zip(generated_data_x, generated_data_y):
        min = func_file.return_value_function([i, j], name_function)
        point_list.append([i, j, min])
        if min < tmp:
            tmp = min
            cord_X = i
            cord_Y = j

    print("X: " + str(cord_X))
    print("Y: " + str(cord_Y))
    print("VALUE: " + str(tmp))

    return point_list
