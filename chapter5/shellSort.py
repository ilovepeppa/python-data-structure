def gap_insert_sort(alist, start, gap):
    for i in range(start + 1, len(alist)):
        current_value = alist[i]
        position = i
        while current_value < alist[position - gap] and position > 0:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = current_value


def shell_sort(alist):
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap):
            gap_insert_sort(alist, i, gap)

        gap //= 2


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(alist)
    print(alist)
