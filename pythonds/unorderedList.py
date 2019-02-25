from pythonds.arrayList import Node, ArrayList


class UnorderedList(ArrayList):
    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def search(self, item):
        current = self.head
        while current and current.get_data() != item:
            current = current.get_next()
        return current is not None
