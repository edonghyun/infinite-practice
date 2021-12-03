import collections
import sys

sys.setrecursionlimit(10**7)


def solution(a, edges):
    if sum(a) != 0:
        return -1

    graph = collections.defaultdict(list)
    for _from, _to in edges:
        graph[_from].append(_to)
        graph[_to].append(_from)

    def dfs(graph, _sum, now, parent, answer):
        local_answer = 0
        for v in graph[now]:
            if v == parent:
                continue
            local_answer += dfs(graph, _sum, v, now, answer)
        _sum[parent] += _sum[now]
        return answer + abs(_sum[now]) + local_answer
    return dfs(graph, a, 0, 0, 0)
