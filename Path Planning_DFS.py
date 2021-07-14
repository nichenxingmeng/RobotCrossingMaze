import numpy as np
from Maze import Maze
from copy import deepcopy

move_map = {
    'u': (-1, 0),
    'r': (0, +1),
    'd': (+1, 0),
    'l': (0, -1),
}

# 深度优先搜索算法
def deepth_first_search(maze, is_visit_m, path, current_loc, result):
    # 到达目标点
    if current_loc == maze.destination:
        result.append(path)
        return

    # 当前可移动方向
    can_move = maze.can_move_actions(current_loc)

    for i in can_move:
        new_loc = tuple(current_loc[j] + move_map[i][j] for j in range(2))

        # 新位置如遍历过则跳过
        if is_visit_m[new_loc]:
            continue

        # 遍历新位置
        is_visit_m[new_loc] = 1
        temp_path = deepcopy(path)
        temp_loc = new_loc
        path.append(i)

        # 搜索
        deepth_first_search(maze, is_visit_m, path, new_loc, result)

        # 回溯
        is_visit_m[temp_loc] = 0
        path = deepcopy(temp_path)

def my_search(maze):
    """
    任选深度优先搜索算法、最佳优先搜索（A*)算法实现其中一种
    :param maze: 迷宫对象
    :return :到达目标点的路径 如：["u","u","r",...]
    """

    path = []

    # -----------------请实现你的算法代码--------------------------------------
    start = maze.sense_robot()
    h, w, _ = maze.maze_data.shape
    is_visit_m = np.zeros((h, w), dtype=np.int)
    result = []

    deepth_first_search(maze, is_visit_m, path, start, result)
    path = result[0]
    # -----------------------------------------------------------------------
    return path