# https://programmers.co.kr/learn/courses/30/lessons/12952

def is_possible(board, _, depth):
    for row, col in enumerate(board):
        if row >= depth:
            continue
        if col == _ or abs(row - depth) == abs(col - _):
            return False
    return True


def solution(n):
    answer = 0
    board = [9999 for _ in range(n)]

    def dfs(board, depth):
        board = board[:]
        result = 0
        for _ in range(n):
            if not is_possible(board, _, depth):
                continue

            if n == depth + 1:
                result += 1
                continue

            board[depth] = _
            result += dfs(board, depth + 1)
        return result

    answer += dfs(board, 0)
    return answer
