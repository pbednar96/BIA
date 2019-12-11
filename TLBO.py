import random
import numpy as np

import static_data
import func_file
import show_3D_graph

POPSIZE = 20
FUNC = "ackley"
DIM = 2
GENERATION = 100


def generate_first_population(func, popsize, dimension):
    population = []
    for i in range(0, popsize):
        gen_point = list(np.random.uniform(static_data.get_min_range(func), static_data.get_max_range(func), dimension))
        evaluate = func_file.return_value_function(gen_point, func)
        population.append([gen_point, evaluate])
    return population


def evaluate_fitness(pop, func):
    return func_file.return_value_function(pop, func)


def get_best_in_population(population):
    best_in_pop = population[0]
    for i in range(len(population)):
        if population[i][1] < best_in_pop[1]:
            best_in_pop = population[i]
    return best_in_pop


def TLBO(func, popsize, dim, max_generation):
    pop = generate_first_population(func, popsize, dim)

    # for graph
    all_points = []
    points_for_graph = [point[0] for point in pop]
    all_points.append(points_for_graph)

    for generation in range(max_generation):
        next_gen = []
        teacher = get_best_in_population(pop)
        x_mean = [sum([i[0][d] for i in pop]) / popsize for d in range(dim)]

        pop.remove(teacher)

        for i in range(popsize - 1):
            new_student = [pop[i][0][d] + random.random() * (teacher[0][d] - (round(1 + random.random())) * x_mean[d])
                           for d in range(dim)]
            new_learner_value = evaluate_fitness(new_student, func)
            if new_learner_value < pop[i][1]:
                pop[i] = [new_student[:], new_learner_value]

        for i in range(popsize - 1):
            j = random.randint(0, popsize - 2)
            new_student = [pop[i][0][d] + random.random() * abs(pop[i][0][d] - pop[j][0][d]) for d in range(dim)]
            new_learner_value = evaluate_fitness(new_student, func)
            if new_learner_value < pop[i][1]:
                next_gen.append([new_student, new_learner_value])
            else:
                next_gen.append(pop[i])

        next_gen.append(teacher)
        pop = next_gen
        points_for_graph = [point[0] for point in pop]
        all_points.append(points_for_graph)

    return all_points, get_best_in_population(pop)


def main():
    point_graph, best_point = TLBO(FUNC, POPSIZE, DIM, GENERATION)
    print(best_point)
    show_3D_graph.animate_in_graph_3D(FUNC, point_graph)

if __name__ == "__main__":
    main()
