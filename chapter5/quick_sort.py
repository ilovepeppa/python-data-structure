def quick_sort(alist):
    if len(alist) <= 1:
        return alist

    left_half = [x for x in alist if x < alist[0]]
    right_half = [x for x in alist if x > alist[0]]

    return quick_sort(left_half) + [alist[0]] + quick_sort(right_half)


def quick_sort_v2(alist, start, end):
    if end <= start:
        return

    left = start + 1
    right = end

    while True:
        while left <= right and alist[left] <= alist[start]:
            left += 1
        while left <= right and alist[right] >= alist[start]:
            right -= 1

        if left > right:
            break

        alist[left], alist[right] = alist[right], alist[left]

    alist[start], alist[right] = alist[right], alist[start]

    quick_sort_v2(alist, start, right - 1)
    quick_sort_v2(alist, right + 1, end)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort_v2(alist, 0, len(alist) - 1)
    print(alist)
