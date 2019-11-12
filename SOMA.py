import numpy as np
import random

import func_file
import static_data
import show_3D_graph

# FUNC = "rastrigin"
FUNC = "ackley"

# SOMA PARAMS
PATHLENGHT = 1.5
STEP = 0.112
POPSIZE = 10
PRT = 0.6
MIGRATIONS = 30
MINDIV = -1
DIM = 2

# missing restriction - out of the bound

def SOMA(func, popsize, dimension):
    population = generate_first_population(func, popsize, dimension)
    point_for_graph = []
    for i in range(MIGRATIONS):
        leader = find_leader_in_population(population, func)
        final_population = []
        for point in population:
            if leader == point:
                final_population.append(point)
            else:
                prt_vector = generate_prt_vector()
                route_points = []
                for step in range(int(PATHLENGHT / STEP)):
                    x = []
                    for v_index, v_value in enumerate(prt_vector):
                        value = point[v_index] + (leader[v_index] - point[v_index]) * step * STEP * v_value
                        x.append(value)
                    route_points.append(x)
                final_population.append(find_best_on_route(route_points, func))
        population = final_population
        point_for_graph.append(final_population)
    print(population)

    show_3D_graph.animate_in_graph_3D(func, point_for_graph)
    print("END")


def generate_prt_vector():
    prt_vector = []
    for i in range(DIM):
        r = random.uniform(0, 1)
        if r < PRT:
            prt_vector.append(1)
        else:
            prt_vector.append(0)
    return prt_vector


def find_best_on_route(route_points, func):
    min_value = func_file.return_value_function(route_points[0], func)
    min_point = route_points[0]
    for point in route_points:
        if func_file.return_value_function(point, func) < min_value:
            min_point = point
    return min_point


def find_leader_in_population(population, func):
    min_value = func_file.return_value_function(population[0], func)
    leader = population[0]
    for point in population:
        if func_file.return_value_function(point, func) < min_value:
            leader = point
    return leader


def generate_first_population(func, popSize, dimension):
    population = []
    for i in range(0, popSize):
        gen_point = list(np.random.uniform(static_data.get_min_range(func), static_data.get_max_range(func), dimension))
        population.append(gen_point)
    return population


def main():
    SOMA(FUNC, POPSIZE, DIM)


if __name__ == "__main__":
    main()
