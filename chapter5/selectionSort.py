def selection_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        max_position = 0
        for j in range(1, i + 1):
            if alist[j] > alist[max_position]:
                max_position = j

        alist[max_position], alist[i] = alist[i], alist[max_position]


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(alist)
    print(alist)
