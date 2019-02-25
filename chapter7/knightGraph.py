from pythonds.graph import Graph


def pos_to_node_id(row, column, size):
    return row * size + column


def get_legal_moves(row, col, size):
    new_moves = []
    move_offsets = [
        [-1, 0], [1, 0], [0, -1], [0, 1],
        [-1, -2], [-1, 2], [1, -2], [1, 2]
    ]
    for offset in move_offsets:
        move_row = row + offset[0]
        move_col = col + offset[1]
        if 0 <= move_row < size and 0 <= move_col < size:
            new_moves.append((move_row, move_col))
    return new_moves


def knight_graph(bd_size):
    kt_graph = Graph()
    for row in range(bd_size):
        for col in range(bd_size):
            note_id = pos_to_node_id(row, col, bd_size)
            new_position = get_legal_moves(row, col, bd_size)
            for e in new_position:
                nid = pos_to_node_id(e[0], e[1], bd_size)
                kt_graph.add_edge(note_id, nid)

    return kt_graph


def dfs(start, time=0):
    time += 1
    start.set_color('grey')
    start.set_discover(time)
    for v in start.get_connections():
        if v.get_color() == 'white':
            v.set_predecessor(start)
            dfs(v, time)
    start.set_color('black')
    time += 1
    start.set_finish(time)


if __name__ == '__main__':
    g = knight_graph(5)
    start = g.get_vertex(0)
    dfs(start)
