# https://programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key


def solution(numbers):
    if all([
        x == 0 for x in numbers
    ]):
        return "0"

    def compare(x, y):
        value_x = x['value']
        value_y = y['value']
        str_x = str(value_x)
        str_y = str(value_y)
        padded_x = x['padded']
        padded_y = y['padded']

        if str_y.find(str_x) == 0 or str_x.find(str_y) == 0:
            return int(str_y + str_x) - int(str_x + str_y)

        if padded_x == padded_y:
            return value_y - value_x
        return padded_y - padded_x

    answer = ''
    numbers.sort(reverse=True)
    max_number = numbers.pop(0)
    numbers.append(max_number)

    digit = len(str(max_number))

    padded_numbers = []
    for number in numbers:
        padded_numbers.append({
            'value': number,
            'padded': int(
                str(
                    number
                ).ljust(digit, str(number)[-1])
            )
        })

    padded_numbers.sort(
        key=cmp_to_key(compare),
    )

    while padded_numbers:
        answer += str(padded_numbers.pop(0)['value'])

    return answer
