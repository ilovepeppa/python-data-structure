def quick_sort(alist):
    if len(alist) <= 1:
        return alist

    left_half = [x for x in alist if x < alist[0]]
    right_half = [x for x in alist if x > alist[0]]

    return quick_sort(left_half) + [alist[0]] + quick_sort(right_half)


def quick_sort_v2(alist):
    if len(alist) <= 1:
        return

    left = 1
    right = len(alist) - 1

    while left < right:
        if alist[left] < alist[0]:
            left += 1
        else:
            alist[left], alist[right] = alist[right], alist[left]
            right -= 1

    alist[0], alist[right] = alist[right], alist[0]

    # quick_sort_v2(alist[:right])
    # quick_sort_v2(alist[right + 1:])


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort_v2(alist)
    print(alist)
