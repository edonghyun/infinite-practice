def is_right_matched(string):
    if string[0] == ")":
        return False

    string = list(string)
    char = string.pop(0)
    stack = [char]
    while string:
        char = string.pop(0)

        if char == stack[0]:
            stack.append(char)
        else:
            stack.pop(0)

    return False if len(stack) > 0 else True


def solve(string):
    left_count = 0
    right_count = 0

    temp_string = ""
    left_string = ""
    for index, c in enumerate(string):
        if c == "(":
            left_count += 1
        if c == ")":
            right_count += 1

        if left_count == right_count:
            temp_string = string[:index+1]
            left_string = string[index+1:]
            break

    if not temp_string:
        return left_string

    left_string = solve(left_string)
    if is_right_matched(temp_string):
        return temp_string + left_string
    else:
        temp_string = temp_string[1:len(temp_string)-1]
        converted = ""
        for char in temp_string:
            if char == "(":
                converted += ")"
            else:
                converted += "("
        return f"({left_string}){converted}"


def solution(p):
    if not p:
        return p
    return solve(p)
