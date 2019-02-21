class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class ArrayList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def remove(self, item):
        current = self.head
        prev = None
        while current and current.get_data() != item:
            prev = current
            current = current.get_next()

        if current is None:
            return

        if prev is None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())

    def add(self, item):
        raise NotImplementedError

    def search(self, item):
        raise NotImplementedError

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.get_data())
            current = current.get_next()
        return str(result)
