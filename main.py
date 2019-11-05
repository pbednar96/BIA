import func_file, static_data, show_3D_graph, blind_search, hill_climbing
from simulated_annealing import simulated_annealing

FUNCTION = "ackley"
NUM_GENERETED_POINTS = 20


def main():
    print("BIA  2019/2020 - BED0111")

    # (2/2)
    # changed and no tested
    # as graph with minumum point + animation points
    # all_points = blind_search.blind_search(FUNCTION, NUM_GENERETED_POINTS)
    # minumum_point = blind_search.blind_search_points(FUNCTION, NUM_GENERETED_POINTS)
    # show_3D_graph.show_both_graph(FUNCTION, all_points, minumum_point)
    ###############################

    # (4/4)
    # hill climbing with recursion
    x = hill_climbing.hill_climbing(FUNCTION, 5, 5, 0.8, 50, 15)
    show_3D_graph.show_graph_with_point(FUNCTION,x)
    # simulated annealing with temperature
    x = simulated_annealing(FUNCTION, 5, 5, 0.8, 50, 1, 200)
    show_3D_graph.show_graph_with_point(FUNCTION, x)
    ##############################


if __name__ == "__main__":
    main()
