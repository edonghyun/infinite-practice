# https://programmers.co.kr/learn/courses/30/lessons/43105

import collections


def get_max(triangle, depth, index):
    if depth == 0:
        return triangle[0][0]

    max_value = None
    if index == 0:
        max_value = get_max(triangle, depth-1, 0)
    elif index == depth:
        max_value = get_max(triangle, depth-1, index-1)
    else:
        max_value = max(
            get_max(triangle, depth-1, index-1),
            get_max(triangle, depth-1, index),
        )
    return triangle[depth][index] + max_value


def get_recursive_answer(triangle):
    answer = 0

    depth = len(triangle)-1
    answer = max(
        get_max(triangle, depth, index) for index, value in enumerate(
            triangle[depth]
        )
    )
    return answer


def get_iterative_answer(triangle):
    dp = {}
    for i, rows in enumerate(triangle):
        for j, current_value in enumerate(rows):
            index = f'{i}:{j}'

            if i == 0 and j == 0:
                print(current_value)
                dp[index] = current_value
            elif j == 0:
                dp[index] = \
                    current_value + dp[f'{i-1}:{j}']
            elif j == i:
                dp[index] = current_value + dp[f'{i-1}:{j-1}']
            else:
                dp[index] = current_value + max(
                    dp[f'{i-1}:{j-1}'],
                    dp[f'{i-1}:{j}'],
                )
    return max([
        dp[f'{len(triangle)-1}:{i}'] for i in range(len(triangle))
    ])


def solution(triangle):
    return get_iterative_answer(triangle)
