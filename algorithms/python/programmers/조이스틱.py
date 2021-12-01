# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    def get_nearest_index(container, name, current_index):
        if current_index == len(container) - 1:
            return

        window = 1
        right = current_index + 1
        left = current_index - 1

        while True:
            if name[right] != 'A' and container[right] != name[right]:
                return (right, window, )
            right += 1
            if name[left] != 'A' and container[left] != name[left]:
                return (left, window, )
            left -= 1
            window += 1

    answer = 0
    input_name = ['A' for a in name]
    upper_letters = ['N', 'O', 'P', 'Q', 'R',
                     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    index = 0
    index_to_next = 0

    t = 0
    while True:
        if name == ''.join(input_name):
            break

        current_letter = input_name[index]
        target_letter = name[index]
        if current_letter != target_letter:
            delta = ord(target_letter) - ord(current_letter)
            if delta <= 13:
                answer += delta
            else:
                answer += (ord('Z') - ord(target_letter) + 1)
            input_name[index] = name[index]
        else:
            index_to_next, amount = get_nearest_index(
                input_name,
                name,
                index,
            )

            answer += amount
            index = index_to_next
    return answer
