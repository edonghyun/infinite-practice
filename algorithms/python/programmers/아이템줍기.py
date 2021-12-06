# https://programmers.co.kr/learn/courses/30/lessons/87694#

import sys

sys.setrecursionlimit(10**7)

BOARD_MAX = 102

direction = [
    # up, down, left, right
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),

    # up-left, up-right, down-left, down-right
    (-1, 1),
    (1, 1),
    (-1, -1),
    (1, -1),
]


def solution(rectangle, characterX, characterY, itemX, itemY):
    # get initial board with rectangles
    board = [[0 for _ in range(BOARD_MAX)] for __ in range(BOARD_MAX)]
    for x1, y1, x2, y2 in rectangle:
        x1 = x1 * 2
        y1 = y1 * 2
        x2 = x2 * 2
        y2 = y2 * 2
        for index in range(x1, x2+1):
            board[y1][index] = 1
            board[y2][index] = 1
        for index in range(y1, y2+1):
            board[index][x1] = 1
            board[index][x2] = 1

    # exlucde inner edges
    new_board = [[0 for _ in range(BOARD_MAX)] for __ in range(BOARD_MAX)]
    visited = ['0:0']
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            id_string = f'{nx}:{ny}'
            if nx > BOARD_MAX - 1 or ny > BOARD_MAX - 1 \
                    or nx < 0 or ny < 0 or id_string in visited:
                continue

            visited.append(id_string)
            if board[ny][nx] == 1:
                new_board[ny][nx] = 1
                continue
            q.append((nx, ny))

    def dfs(x, y, depth, visited, reverse=False):
        if x == itemX * 2 and y == itemY * 2:
            return depth

        local_direction = direction[:4]
        if reverse:
            local_direction.reverse()

        for dx, dy in local_direction:
            nx = x + dx
            ny = y + dy
            id_string = f'{nx}:{ny}'

            if nx > BOARD_MAX - 1 or ny > BOARD_MAX - 1 \
                    or nx < 0 or ny < 0 or id_string in visited:
                continue

            if new_board[ny][nx] == 1:
                visited.append(id_string)
                r = dfs(
                    nx,
                    ny,
                    depth+1,
                    visited,
                    reverse=reverse,
                )
                if r:
                    return r

    return min(
        dfs(characterX * 2, characterY * 2, 0, [], reverse=False),
        dfs(characterX * 2, characterY * 2, 0, [], reverse=True)
    ) / 2
