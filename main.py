import func_file, static_data, show_3D_graph, blind_search, hill_climbing
from simulated_annealing import simulated_annealing

FUNCTION = "levy"
NUM_GENERETED_POINTS = 20


def main():
    # as graph with minumum point + animation points (2/2)
    # all_points = blind_search.blind_search(FUNCTION, NUM_GENERETED_POINTS)
    # minumum_point = blind_search.blind_search_points(FUNCTION, NUM_GENERETED_POINTS)
    # show_3D_graph.show_both_graph(FUNCTION, all_points, minumum_point)

    # x = hill_climbing.hill_climbing(FUNCTION, 5, 5, 0.6, 50, 5)
    # print(x)

    x = simulated_annealing(FUNCTION, 5, 5, 0.6, 50, 15, 200)
    print(x)


if __name__ == "__main__":
    main()
