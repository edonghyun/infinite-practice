# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    while priorities:
        answer += 1
        current_priority = priorities.pop(0)
        if not priorities:
            break

        if current_priority >= max(priorities):
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(current_priority)
            location = len(priorities) - 1 \
                if location == 0 else location - 1
            answer -= 1
    return answer
