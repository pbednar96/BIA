from datetime import datetime


def permutation(list_data):
    list_perm = []
    if len(list_data) == 1:
        return [list_data]
    for i in range(len(list_data)):
        m = list_data[i]
        new_list = list_data[:i] + list_data[i + 1:]
        for p in permutation(new_list):
            list_perm.append([m] + p)
    return list_perm


def main():
    data = [1, 2, 3]
    start_time = datetime.now()
    print(permutation(data))
    end_time = datetime.now()
    print(str(end_time - start_time))


if __name__ == "__main__":
    main()
