from datetime import datetime


def permutation(list_data):
    l = []
    if len(list_data) == 1:
        return [list_data]
    for i in range(len(list_data)):
        m = list_data[i]
        new_list = list_data[:i] + list_data[i + 1:]
        for p in permutation(new_list):
            l.append([m] + p)
    return l


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    start_time = datetime.now()
    for p in permutation(data):
        item = p
    end_time = datetime.now()

    print(str(end_time - start_time))


if __name__ == "__main__":
    main()
