import math
import numpy as np

import func_file
import static_data

POPSIZE = 20
FUNC = "ackley"
DIM = 2
GENERATION = 100


def generate_first_population(popsize, dimension):
    population = []
    for i in range(0, popsize):
        gen_point = list(np.random.uniform(-55, 55, dimension))
    return population


def f1(point):
    return -point ** 2


def f2(point):
    return -(point - 2) ** 2


def NSGA2(popsize, dim):
    random_solution = generate_first_population(popsize, dim)

    solution_f1_pop = [f1(solution) for solution in random_solution]
    solution_f2_pop = [f2(solution) for solution in random_solution]
    np = []
    sp = []
    print(solution_f2_pop)
    for i in range(len(solution_f1_pop)):
        n = 0
        s = []
        for j in range(len(solution_f2_pop)):
            print(j)
            print(i)
            if i != j:
                print('x')
                if solution_f1_pop[i] > solution_f1_pop[j] and solution_f1_pop[i] > solution_f1_pop[j]:
                    n += 1
                    print('yes')
                if solution_f1_pop[i] < solution_f1_pop[j] and solution_f1_pop[i] < solution_f1_pop[j]:
                    s.append(j)
                    print('no')
        np.append(n)
        sp.append(s)
    print(np)
    print(sp)

def main():
    NSGA2(POPSIZE, DIM)

if __name__ == "__main__":
    main()
