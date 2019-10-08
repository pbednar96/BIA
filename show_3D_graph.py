# PYTHON IMPORT
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation


# need rework

def show_graph(name_function):
    # MY IMPORT
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

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


def show_both_graph(name_function, list_points):
    show_graph(name_function)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # ax = Axes3D(fig)
    # for i in range(len(list_points)):
    #     ax.scatter(list_points[i][0], list_points[i][1], list_points[i][2])

    def animate(i):
        if i > len(list_points):
            pass
        else:
            ax.scatter(list_points[i][0], list_points[i][1], list_points[i][2])
        return ax

    ani = FuncAnimation(fig, animate, frames=len(list_points), interval=200)

    plt.show()
