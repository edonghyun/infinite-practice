def solution(board):
    direction_y, direction_x = (0, 0, -1, 1), (1, -1, 0, 0)
    width = len(board)

    def dfs(start_y, start_x, cost, direction):
        result = [[9999999 for _ in range(width)] for _ in range(width)]
        result[start_y][start_x] = 0

        queue = [(start_y, start_x, cost, direction)]
        while queue:
            y, x, cost, direction = queue.pop(0)
            for i in range(4):
                next_y = y + direction_y[i]
                next_x = x + direction_x[i]
                next_cost = cost + 100 if direction == i else cost + 600
                if next_y >= 0 and next_x >= 0 and \
                        next_y < width and next_x < width and \
                        board[next_y][next_x] == 0 and \
                        result[next_y][next_x] > next_cost:
                    result[next_y][next_x] = next_cost
                    queue.append(
                        (next_y, next_x, next_cost, i)
                    )
        return result[-1][-1]
    return min(dfs(0, 0, 0, 0), dfs(0, 0, 0, 3))
