from pythonds.deque import Deque


def palchecker(astring):
    deque = Deque()

    for ch in astring:
        deque.add_rear(ch)

    equal = True
    while deque.size() > 1:
        first = deque.remove_front()
        last = deque.remove_rear()
        if first != last:
            equal = False
            break
    return equal


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
