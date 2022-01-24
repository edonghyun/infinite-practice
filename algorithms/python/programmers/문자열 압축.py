def list_to_string(_list):
    return "".join(_list)


def solve(window_size, string):
    past_string = list_to_string(string[:window_size])
    compressed_string = []
    number = 0
    index = 0
    while index < len(string):
        current_string = list_to_string(string[index:index+window_size])

        if current_string == past_string:
            number += 1
        else:
            compressed = f"{number}{past_string}" if number > 1 else f"{past_string}"
            number = 1
            compressed_string.append(compressed)

        index += window_size
        past_string = current_string

    compressed = f"{number}{past_string}" if number > 1 else f"{past_string}"
    compressed_string.append(compressed)

    return len(list_to_string(compressed_string))


def solution(s):
    t = [
        solve(length, list(s))
        for length in range(1, len(s))
    ]
    return min(t) if t else 1
