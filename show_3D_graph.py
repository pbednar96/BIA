#PYTHON IMPORT
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def show_graph(name_function):
    #MY IMPORT
    import static_data, func_file
    range_list = np.arange(static_data.get_min_range(name_function), static_data.get_max_range(name_function),
                           static_data.get_range(name_function))
    X = [i for i in range_list for _ in range_list]
    Y = list(range_list) * len(range_list)

    if name_function == "ackley":
        Z = [func_file.ackley([x, y]) for x, y in zip(X, Y)]
    elif name_function == "levy":
        Z = [func_file.levy([x, y]) for x, y in zip(X, Y)]
    elif name_function == "rastrigin":
        Z = [func_file.rastrigin([x, y]) for x, y in zip(X, Y)]
    elif name_function == "griewank":
        Z = [func_file.griewank([x, y]) for x, y in zip(X, Y)]
    elif name_function == "schwefel":
        Z = [func_file.schwefel([x, y]) for x, y in zip(X, Y)]
    elif name_function == "zakharov":
        Z = [func_file.zakharov([x, y]) for x, y in zip(X, Y)]
    elif name_function == "sphere":
        Z = [func_file.sphere([x, y]) for x, y in zip(X, Y)]
    elif name_function == "michalewicz":
        Z = [func_file.michalewicz([x, y]) for x, y in zip(X, Y)]


    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_trisurf(X, Y, Z, cmap='inferno', edgecolor='none');

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

