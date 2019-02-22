def binary_search(alist, item):
    start = 0
    end = len(alist) - 1

    found = False
    while start <= end and not found:
        mid = (start + end) // 2
        if alist[mid] > item:
            end = mid - 1
        elif alist[mid] < item:
            start = mid + 1
        else:
            found = True

    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
