# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    times.sort()
    left = 0
    right = times[len(times)-1] * n
    answer = 0
    while left <= right:
        mid = int((left + right) / 2)
        total = 0
        for t in times:
            total += int(mid / t)
        if total < n:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    return answer
