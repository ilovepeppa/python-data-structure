def insertion_sort(alist):
    for i in range(1, len(alist)):
        current_value = alist[i]
        position = i

        while current_value < alist[position - 1] and position > 0:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = current_value


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(alist)
    print(alist)
