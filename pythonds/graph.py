import sys


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white'
        self.distance = sys.maxsize
        self.predecessor = None
        self.discover = 0
        self.finish = 0

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def set_color(self, color):
        self.color = color

    def set_distance(self, distance):
        self.distance = distance

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor

    def set_discover(self, discover):
        self.discover = discover

    def set_finish(self, finish):
        self.finish = finish

    def get_distance(self):
        return self.distance

    def get_color(self):
        return self.color

    def get_predecessor(self):
        return self.predecessor

    def get_discover(self):
        return self.discover

    def get_finish(self):
        return self.finish


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        self.num_vertices += 1
        return new_vertex

    def get_vertex(self, key):
        return self.vert_list.get(key, None)

    def __contains__(self, key):
        return key in self.vert_list

    def add_edge(self, f, t, weight=0):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)


        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def get_vertices(self):
        return self.vert_list.keys()


    def __iter__(self):
        return iter(self.vert_list.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        for w in v.get_connections():
            print('(%s, %s)' % (v.get_id(), w.get_id()))
