from arrayList import Node, ArrayList


class OrderedList(ArrayList):

    def add(self, item):
        tmp = Node(item)
        current = self.head
        prev = None

        while current and current.get_data() < item:
            prev = current
            current = current.get_next()

        tmp.set_next(current)
        if prev is None:
            self.head = tmp
        else:
            prev.set_next(tmp)

    def search(self, item):
        found = False
        current = self.head
        while current:
            if current.get_data() == item:
                found = True
                break
            if current.get_data() > item:
                break
            current = current.get_next()
        return found


a = OrderedList()
a.add('5')
a.add('1')
a.add('0')
a.add('6')
a.add('3')

print(a)