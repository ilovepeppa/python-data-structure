class BinaryHeap:
    def __init__(self):
        self.head_list = [0]
        self.current_size = 0

    def _perc_up(self, i):
        while i // 2 > 0:
            parent = i // 2
            if self.head_list[i] < self.head_list[parent]:
                self.head_list[i], self.head_list[parent] = self.head_list[parent], self.head_list[i]

            i //= 2

    def _perc_down(self, i):
        while 2 * i <= self.current_size:
            min_child = self._min_child(i)
            if self.head_list[min_child] < self.head_list[i]:
                self.head_list[i], self.head_list[min_child] = self.head_list[min_child], self.head_list[i]

            i = min_child

    def _min_child(self, i):
        if 2 * i + 1 > self.current_size:
            return 2 * i
        else:
            return 2 * i if self.head_list[2 * i] < self.head_list[2 * i + 1] else 2 * i + 1

    def insert(self, k):
        self.head_list.append(k)
        self.current_size += 1
        self._perc_up(self.current_size)

    def find_min(self):
        return self.head_list[1]

    def del_min(self):
        if self.current_size < 1:
            return None

        result = self.head_list[1]
        self.head_list[1] = self.head_list[self.current_size]
        self.current_size -= 1
        self.head_list.pop()
        self._perc_down(1)
        return result

    def is_empty(self):
        return self.current_size == 0

    def size(self):
        return self.current_size

    def build_heap(self, alist):
        self.head_list = [0] + alist[:]
        self.current_size = len(alist)
        n = len(alist) // 2
        while n > 0:
            self._perc_down(n)
            n -= 1



if __name__ == '__main__':
    bh = BinaryHeap()
    bh.build_heap([9, 6, 5, 2, 3])
    while bh.size() > 0:
        print(bh.del_min())
