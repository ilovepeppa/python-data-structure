class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected_to = {}
        self.visited = False
        self.predecessor = None
        self.distance = 0
        self.discover = 0
        self.finish = 0

    def add_neighbour(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_neighbours(self):
        return self.connected_to.keys()


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.time = 0

    def add_vertex(self, key):
        self.vertex_list[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vertex_list.get(key, None)

    def add_edge(self, f, t, weight=0):
        if f not in self.vertex_list:
            self.add_vertex(f)

        if t not in self.vertex_list:
            self.add_vertex(t)

        self.vertex_list[f].add_neighbour(self.vertex_list[t], weight)

    def __iter__(self):
        return iter(self.vertex_list.values())

    def dfs(self, start):
        start.visited = True
        self.time += 1
        start.discover = self.time
        for v in start.get_neighbours():
            if not v.visited:
                self.dfs(v)

        self.time += 1

        start.finish = self.time

    def bfs(self, start):
        queue = [start]
        while len(queue) > 0:
            current = queue.pop(0)
            current.visited = True
            for v in current.get_neighbours():
                if not v.visited:
                    v.distance = current.distance + 1
                    v.predecessor = current
                    queue.append(v)
