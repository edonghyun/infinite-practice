def print_board(board):
    for b in board:
        print(b)
    print()


def solution(rows, columns, queries):
    board = [
        [
            (row_index) * columns + (column_index+1)
            for column_index in range(columns)
        ] for row_index in range(rows)
    ]

    answer = []
    for query in queries:
        y1, x1, y2, x2 = [
            q - 1
            for q in query
        ]

        min_value = 999999
        temp_value = None
        next_temp_value = None

        # 상단
        for x_delta in range(x2-x1, -1, -1):
            min_value = min(board[y1][x1 + x_delta], min_value)

            if x_delta == x2-x1:
                temp_value = board[y1][x1 + x_delta]

            if x_delta == 0:
                board[y1][x1 + x_delta] = board[y1 + 1][x1]
            else:
                board[y1][x1 + x_delta] = board[y1][x1 + x_delta-1]

        # 우측
        for y_delta in range(y2-y1, 0, -1):
            min_value = min(board[y1 + y_delta][x2], min_value)

            if y_delta == y2-y1:
                next_temp_value = board[y1 + y_delta][x2]

            if y_delta == 1:
                board[y1 + y_delta][x2] = temp_value
                temp_value = next_temp_value
            else:
                board[y1 + y_delta][x2] = board[y1 + y_delta-1][x2]

        # 하단
        for x_delta in range(0, x2-x1):
            min_value = min(board[y2][x1 + x_delta], min_value)

            if x_delta == 0:
                next_temp_value = board[y2][x1 + x_delta]

            if x_delta == x2-x1-1:
                board[y2][x1 + x_delta] = temp_value
                temp_value = next_temp_value
            else:
                board[y2][x1 + x_delta] = board[y2][x1 + x_delta + 1]

        # 좌측
        for y_delta in range(0, y2-y1):
            if y_delta == 0:
                continue

            min_value = min(board[y1+y_delta][x1], min_value)

            if y_delta == y2-y1-1:
                board[y1+y_delta][x1] = temp_value
            else:
                board[y1+y_delta][x1] = board[y1+y_delta + 1][x1]

        answer.append(min_value)
    return answer
