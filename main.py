import func_file, static_data, show_3D_graph, blind_search

FUNCTION = "sphere"


def main():
    x = blind_search.blind_search(FUNCTION, 20)
    show_3D_graph.show_both_graph(FUNCTION, x)

if __name__ == "__main__":
    main()
