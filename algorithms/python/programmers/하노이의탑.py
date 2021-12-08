# https://programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    def solve(n, a, b):
        if n == 1:
            return [[a, b]]

        numbers = [1, 2, 3]
        numbers.pop(numbers.index(a))
        numbers.pop(numbers.index(b))

        left_number = numbers[0]

        return (
            solve(n-1, a, left_number)
            + [[a, b]]
            + solve(n-1, left_number, b)
        )

    return solve(n, 1, 3)
