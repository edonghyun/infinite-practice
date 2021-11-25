# https://programmers.co.kr/learn/courses/30/lessons/43162

import collections


def solution(n, computers):
    answer = 0

    # graph
    graph = dict()
    for source_index, connections in enumerate(computers):
        graph[source_index] = list()
        for target_index, connection in enumerate(connections):
            if source_index == target_index:
                continue
            if connection == 1:
                graph[source_index].append(target_index)

    # traverse
    q = [0]
    visited = dict()

    for start in graph.keys():
        q = [start]
        if start not in visited:
            answer += 1

        while q:
            source_index = q.pop(0)
            if source_index in visited:
                continue

            visited[source_index] = True
            for target_index in graph[source_index]:
                q.append(target_index)

    return answer
