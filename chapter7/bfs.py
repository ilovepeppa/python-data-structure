from pythonds.graph import Graph, Vertex
from pythonds.queue import Queue


def build_graph(word_file):
    d = {}
    g = Graph()
    with open(word_file) as f:
        for line in f:
            word = line.strip()
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

    for bucket, words in d.items():
        for word1 in words:
            for word2 in words:
                if word1 != word2:
                    g.add_edge(word1, word2)

    return g


def bfs(start):
    start.set_distance(0)
    start.set_predecessor(None)
    vert_queue = Queue()
    vert_queue.enqueue(start)

    while vert_queue.size() > 0:
        current_vert = vert_queue.dequeue()
        for nbr in current_vert.get_connections():
            if nbr.get_color() == 'white':
                nbr.set_color('gray')
                nbr.set_distance(current_vert.get_distance() + 1)
                nbr.set_predecessor(current_vert)
                vert_queue.enqueue(nbr)

        current_vert.set_color('black')


def traverse(g, f, t):
    start = g.get_vertex(f)
    end = g.get_vertex(t)
    bfs(start)

    print(end.get_id())
    while end.get_predecessor():
        end = end.get_predecessor()
        print(end.get_id())


if __name__ == '__main__':
    g = build_graph('chapter7/words.txt')
    traverse(g, 'fool', 'sage')
