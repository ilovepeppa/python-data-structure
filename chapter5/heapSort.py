def _perc_down(alist, size, i):
    while 2 * i <= size:
        max_child = _max_child(alist, size, i)
        if alist[max_child] > alist[i]:
            alist[max_child], alist[i] = alist[i], alist[max_child]
        i = max_child


def _max_child(alist, size, i):
    if 2 * i + 1 > size:
        return 2 * i
    else:
        return 2 * i if alist[2 * i] > alist[2 * i + 1] else 2 * i + 1


def build_max_heap(alist, size):
    n = size // 2
    while n > 0:
        _perc_down(alist, size, n)
        n -= 1


def heap_sort(alist):
    alist.insert(0, 0)
    i = 1
    while i < len(alist):
        build_max_heap(alist, len(alist) - i)
        alist[1], alist[-i] = alist[-i], alist[1]
        i += 1
    alist.pop(0)


a = [5, 1, 3, 6, 2, 10, 4]

heap_sort(a)
print(a)
