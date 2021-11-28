# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    routes.sort(key=lambda x: x[0])
    answer = 0

    start_position, end_position = routes.pop(0)
    answer += 1
    installed_point = end_position
    for start, end in routes:
        if start > installed_point:
            answer += 1
            installed_point = end
        else:
            installed_point = min(end, installed_point)
    return answer
