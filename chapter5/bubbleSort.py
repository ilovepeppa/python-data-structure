def bubble_sort(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


def short_bubble_sort(alist):
    for i in range(len(alist) - 1):
        changed = False
        for j in range(len(alist) - i - 1):
            if alist[j] > alist[j + 1]:
                changed = True
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

        if not changed:
            break


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    short_bubble_sort(alist)
    print(alist)
