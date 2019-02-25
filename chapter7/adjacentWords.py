from pythonds.graphs import Graph


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


def traverse(g, f, t):
    g.bfs(g.get_vertex(f))
    node = g.get_vertex(t)
    print(node.key)
    while node.predecessor:
        node = node.predecessor
        print(node.key)


if __name__ == '__main__':
    g = build_graph('chapter7/words.txt')
    traverse(g, 'fool', 'sage')
