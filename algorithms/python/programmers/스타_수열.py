# https://programmers.co.kr/learn/courses/30/lessons/70130#

import collections
import heapq


def solution(a):
    answer = 0
    mapper = collections.defaultdict(int)
    for e in a:
        mapper[e] += 1
    q = []
    for k, v in mapper.items():
        heapq.heappush(q, (-v, k))
    while q:
        v, k = heapq.heappop(q)
        if mapper[k] < answer:
            continue
        local_answer = 0
        index = 0
        while index < len(a) - 1:
            es = [a[index], a[index+1]]
            if k in es and a[index] != a[index+1]:
                index += 1
                local_answer += 2
            index += 1
        answer = max(answer, local_answer)
    return answer
