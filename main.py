import func_file, static_data, show_3D_graph, blind_search

FUNCTION = "sphere"
NUM_GENERETED_POINTS = 20


def main():
    # x = blind_search.blind_search_point(FUNCTION, NUM_GENERETED_POINTS)
    # show_3D_graph.show_graph(FUNCTION, x)
    #
    x = blind_search.blind_search(FUNCTION, NUM_GENERETED_POINTS)
    show_3D_graph.show_both_graph(FUNCTION, x)


if __name__ == "__main__":
    main()
