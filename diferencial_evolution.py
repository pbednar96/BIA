import random
import numpy as np

import static_data
import func_file
from show_3D_graph import show_graph_with_points

DIMENSIONS = 2
POPSIZE = 20
MUTATION = 0.5
GENERATIONS = 100
FUNC = "ackley"
SCALING_VECTOR = 0.5
CR = 0.6

def de(func, dimension, popsize, generations, scaling_vector):
    population = generate_first_popilation(func, popsize, dimension)
    num_generation = 0
    while generations > num_generation:
        new_population = []
        for i in range(0, popsize):
            parent = random.sample(range(0, popsize), 3)

            parents = [population[x] for x in parent]
            mutation_v = mutation_pop(parents, dimension, scaling_vector)

            child = []
            for index in range(dimension):
                r = random.uniform(0, 1)
                if r <= CR:
                    child.append(mutation_v[index])
                else:
                    child.append(population[i][index])

            if func_file.return_value_function(child, func) < func_file.return_value_function(population[i], func):
                new_population.append(child)
            else:
                new_population.append(population[i])

        population = new_population
        num_generation += 1
        print(num_generation)
        print(population)
    return population


def generate_first_popilation(func, popSize, dimension):
    population = []
    for i in range(0, popSize):
        gen_point = list(np.random.uniform(static_data.get_min_range(func), static_data.get_max_range(func), dimension))
        population.append(gen_point)
    return population


def mutation_pop(parents, dimension, scaling_vector):
    mutation_v = []
    # print(parents)
    for j in range(0, dimension):
        mutation_v.append(parents[0][j] + scaling_vector * (parents[1][j]) - parents[2][j])
    return mutation_v


def main():
    final_points = de(FUNC, DIMENSIONS, POPSIZE, GENERATIONS, SCALING_VECTOR)
    show_graph_with_points(FUNC, final_points)


if __name__ == "__main__":
    main()
