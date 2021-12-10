# https://programmers.co.kr/learn/courses/30/lessons/12927

import heapq


def solution(n, works):
    q = []
    for t in works:
        heapq.heappush(q, (-t, t))

    for i in range(n):
        element = heapq.heappop(q)[1]
        new = element - 1
        if new < 0:
            break
        heapq.heappush(q, (-new, new))

    result = 0
    while q:
        result += (heapq.heappop(q)[1] ** 2)
    return result
