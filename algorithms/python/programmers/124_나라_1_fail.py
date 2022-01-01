def update(_list):
    for index in range(len(_list)-1, 0, -1):
        if _list[index] > 3:
            _list[index] = 1
            _list[index-1] += 1
    if _list[0] > 3:
        _list[0] = 1
        _list = [1] + _list
    return _list


def solution(n):
    answer = [1]
    index = 1
    while index < n:
        answer[-1] += 1
        if answer[-1] > 3:
            answer = update(answer)
        index += 1

    translated = ""
    for n in answer:
        if n == 3:
            translated += "4"
        else:
            translated += str(n)
    return translated
