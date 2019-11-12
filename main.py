import func_file, static_data, show_3D_graph, blind_search, hill_climbing
from simulated_annealing import simulated_annealing

FUNCTION = "ackley"
NUM_GENERETED_POINTS = 20


def main():
    print("BIA  2019/2020 - BED0111")

    # Blind search
    # get best point and show in 3d graph
    searched_points = blind_search.blind_search(FUNCTION, NUM_GENERETED_POINTS)
    show_3D_graph.show_graph_with_searched_point_3D(FUNCTION, searched_points)
    ###############################

    # (4/4)
    # hill climbing with recursion
    x = hill_climbing.hill_climbing(FUNCTION, 5, 5, 0.8, 50, 15)
    show_3D_graph.show_graph_with_searched_point_3D(FUNCTION, x)
    # simulated annealing with temperature
    x = simulated_annealing(FUNCTION, 5, 5, 0.8, 1, 200)
    show_3D_graph.show_graph_with_searched_point_3D(FUNCTION, x)
    ##############################


if __name__ == "__main__":
    main()
