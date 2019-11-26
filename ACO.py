import math
import numpy as np
import random
import matplotlib.pyplot as plt

FILENAME = "datasets/tps_dataset.txt"

ITERATIONS = 200
NUM_ANTS = 50
EVAPORATION = 0.5
ALPHA = 1
BETA = 2


def get_list_values(filename):
    with open(filename, 'r') as f:
        all_lines = [[int(num) for num in line.split()] for line in f]
    return all_lines


def distance(node1, node2):
    return math.sqrt(((node1[1] - node2[1]) ** 2) + ((node1[2] - node2[2]) ** 2))


def first_matrix_visibility(matrix):
    visibility = 1 / matrix
    visibility[visibility == np.inf] = 0
    return visibility


def create_matrix(list_nodes):
    matrix = np.zeros((len(list_nodes), len(list_nodes)))
    for j in range(len(list_nodes)):
        for i in range(len(list_nodes)):
            if j != i:
                matrix[i, j] = distance(list_nodes[i], list_nodes[j])
                matrix[j, i] = distance(list_nodes[i], list_nodes[j])

    matrix.tolist()
    return matrix


def cal_total_dist(list_points, matrix):
    sum = 0
    for i in range(18):
        sum += matrix[int(list_points[i]) - 1][int(list_points[i + 1]) - 1]
    return sum


def ACO(filename, num_ants, iter, alpha, beta, evap):
    matrix = create_matrix(get_list_values(filename))
    num_cities = len(matrix[0])
    visibility = first_matrix_visibility(matrix)
    pheromne = .1 * np.ones((num_ants, num_cities))
    route = np.ones((num_ants, num_cities + 1))
    for _ in range(iter):
        route[:, 0] = 1
        for i in range(num_ants):
            temp_visibility = np.array(visibility)
            for j in range(num_cities - 1):
                cur_loc = int(route[i, j] - 1)
                temp_visibility[:, cur_loc] = 0
                p_feature = np.power(pheromne[cur_loc, :], beta)
                v_feature = np.power(temp_visibility[cur_loc, :], alpha)
                p_feature = p_feature[:, np.newaxis]
                v_feature = v_feature[:, np.newaxis]

                combine_feature = np.multiply(p_feature, v_feature)
                total = np.sum(combine_feature)
                probs = combine_feature / total
                cum_prob = np.cumsum(probs)
                r = random.uniform(0, 1)
                city = np.argmax(cum_prob > r) + 1
                route[i, j + 1] = city

        dist_route = np.zeros((num_ants, 1))
        for i in range(num_ants):
            dist_route[i] = cal_total_dist(route[i], matrix)
        dist_min_loc = np.argmin(dist_route)
        best_route = route[dist_min_loc, :]
        pheromne = (1 - evap) * pheromne
        for i in range(num_ants):
            for j in range(num_cities - 1):
                dt = 1 / dist_route[i]
                pheromne[int(route[i, j]) - 1, int(route[i, j + 1]) - 1] = pheromne[int(route[i, j]) - 1, int(
                    route[i, j + 1]) - 1] + dt
    best_route.tolist()
    best_route = [int(x) for x in best_route]
    return best_route


def show_final_graph(final_route, filename):
    list_nodes = get_list_values(filename)
    x = []
    y = []
    for i in list_nodes:
        x.append(i[1])
        y.append(i[2])
    plt.plot(x, y, "go")
    for i in range(len(final_route) - 1):
        plt.plot([x[final_route[i] - 1], x[final_route[i + 1] - 1]], [y[final_route[i] - 1], y[final_route[i + 1] - 1]],
                 'k-')
    plt.plot([x[final_route[19] - 1], x[final_route[0] - 1]], [y[final_route[19] - 1], y[final_route[0] - 1]], 'k-')
    plt.show()


def main():
    matrix = create_matrix(get_list_values(FILENAME))
    best_route = ACO(FILENAME, NUM_ANTS, ITERATIONS, ALPHA, BETA, EVAPORATION)
    print(f'Best route: {best_route}')
    dist = cal_total_dist(best_route, matrix)
    print(f'Distance route: {dist}')
    show_final_graph(best_route, FILENAME)


if __name__ == "__main__":
    main()
