def anagram_solution1(s1, s2):
    alist = list(s2)
    ok = True

    for c1 in s1:
        found = False
        for i, c2 in enumerate(alist):
            if c1 == c2:
                alist[i] = None
                found = True
                break

        if not found:
            ok = False
            break

    return ok and len([i for i in alist if i is not None]) == 0


def anagram_solution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    matches = True

    for i in range(len(alist1)):
        if alist1[i] != alist2[i]:
            matches = False
            break

    return matches


def anagram_solution3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i, ch in enumerate(s1):
        pos = ord(ch) - ord('a')
        c1[pos] = c1[pos] + 1

    for i, ch in enumerate(s2):
        pos = ord(ch) - ord('a')
        c2[pos] = c2[pos] + 1

    return c1 == c2


print(anagram_solution3('abcd', 'dcab'))
