# PYTHON IMPORT
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def show_graph_with_searched_point_3D(name_function, point):
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
    ax.scatter(point[0],point[1],point[2])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


def animate_in_graph_3D(name_function, points):
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

    ax.plot_trisurf(X, Y, Z, cmap='inferno', edgecolor='none')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    def animate(i):
        ax.clear()

        ax.plot_trisurf(X, Y, Z, cmap='inferno', edgecolor='none')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        for j in range(len(points[0])):
            ax.scatter(points[i][j][0], points[i][j][1])
        return ax

    ani = FuncAnimation(fig, animate, frames=len(points), interval=400, repeat=False)


    plt.show()
