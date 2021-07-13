import numpy as np

move_map = {
    'u': (-1, 0),
    'r': (0, +1),
    'd': (+1, 0),
    'l': (0, -1),
}

class SearchTree(object):
    def __init__(self, loc=(), action='', parent=None):
        self.loc = loc
        self.to_this_action = action
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def is_leaf(self):
        return len(self.children) == 0

def expand(maze, is_visit_m, node):
    can_move = maze.can_move_actions(node.loc)
    for a in can_move:
        new_loc = tuple(node.loc[i] + move_map[a][i] for i in range(2))
        if not is_visit_m[new_loc]:
            child = SearchTree(loc=new_loc, action=a, parent=node)
            node.add_child(child)

def back_propagation(node):
    path = []
    while node.parent is not None:
        path.insert(0, node.to_this_action)
        node = node.parent
    return path

def breadth_first_search(maze):
    start = maze.sense_robot()
    root = SearchTree(loc=start)
    queue = [root]
    h, w, _ = maze_data.shape
    is_visit_m = np.zeros((h, w), dtype=np.int)
    path = []
    while True:
        current_node = queue[0]
        is_visit_m[current_node.loc] = 1

        if current_node.loc == maze.destination:
            path = back_propagation(current_node)
            break

        if current_node.is_leaf():
            expand(maze, is_visit_m, current_node)

        for child in current_node.children:
            queue.append(child)

        queue.pop(0)

    return path



















