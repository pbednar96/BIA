import random
import numpy as np
import math

import static_data
import func_file
import show_3D_graph

POPSIZE = 15
FUNC = "rastrigin"
DIM = 2
MAXGEN = 30
BETA = 0.2
ALPHA = 0.1
OMEGA = 1


def generate_first_population(func, popSize, dimension):
    population = []
    for i in range(0, popSize):
        gen_point = list(np.random.uniform(static_data.get_min_range(func), static_data.get_max_range(func), dimension))
        evaluate = func_file.return_value_function(gen_point, func)
        population.append([gen_point, evaluate])
    return population


def evaluate_fitness(func, population):
    x = [func_file.return_value_function(pop, func) for pop in population]
    return x


def get_best_in_population(population):
    best_in_pop = population[0]
    for i in range(len(population)):
        if population[i][1] < best_in_pop[1]:
            best_in_pop = population[i]
    return best_in_pop


def distance(node1, node2):
    dist = [(node1[i] - node2[i]) ** 2 for i in range(len(node1))]
    return math.sqrt(sum(dist))


def movement(j, k, dim):
    alpha = ALPHA
    beta = BETA
    omega = OMEGA
    r = distance(j[0], k[0])
    psi = random.uniform(0.4, 0.5)
    j = [j[tr] + beta * (1 / (omega + r)) * (k[tr] - j[tr]) + alpha * (psi - 0.5) for tr in range(dim)]
    return j


def eFA(func, popsize, dim, maxgen):
    alpha = ALPHA
    beta = BETA
    omega = OMEGA

    pop = generate_first_population(func, popsize, dim)
    all_points = []

    points = [point[0] for point in pop]
    all_points.append(points)

    i = 0

    while (i < maxgen):
        current_best = get_best_in_population(pop)
        for index, j in enumerate(pop):
            for k in pop:
                r = distance(j[0], k[0])
                if j[1] > k[1]:
                    psi = random.uniform(0, 1)
                    j[0] = [j[0][tr] + beta * (1 / (omega + r)) * (k[0][tr] - j[0][tr]) + alpha * (psi - 0.5) for tr in
                            range(dim)]
            j[1] = func_file.return_value_function(j[0], func)

        if current_best > get_best_in_population(pop):
            current_best = get_best_in_population(pop)
        # for graph
        points = [point[0] for point in pop]
        all_points.append(points)
        i += 1

    print(current_best)
    show_3D_graph.animate_in_graph_3D(func, all_points)


def main():
    eFA(FUNC, POPSIZE, DIM, MAXGEN)


if __name__ == "__main__":
    main()
