def check(
    start_y, 
    start_x,
    total_width,
    key, 
    lock, 
    lock_start_index, 
    lock_end_index
):
    total_map = [
        [0 for _ in range(total_width)]
            for _ in range(total_width)
    ]
    for i, row in enumerate(key):
        for j, col in enumerate(row):
            total_map[i+start_y][j+start_x] = key[i][j]
    
    for i, row in enumerate(lock):
        for j, col in enumerate(row):
            total_map[lock_start_index + i][lock_start_index + j] += col
            if total_map[lock_start_index + i][lock_start_index + j] != 1:
                return False
    return True

def print_graph(data):
    for row in data:
        print(row)
    print()
    
def rotate(data):
    length = len(data)
    copied = [
        [0 for _ in range(len(data))]
            for _ in range(len(data))
    ]
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            copied[j][length-i-1] = col
    return copied

def solution(key, lock):
    answer = False
    total_width = 2 * (len(key) - 1) + len(lock)
    lock_start_index = len(key) - 1
    lock_end_index = lock_start_index + len(lock)
     
    for _ in range(4):
        key = rotate(key)
        for i in range(lock_end_index):
            for j in range(lock_end_index):
                if check(
                    i,
                    j,
                    total_width,
                    key,
                    lock,
                    lock_start_index,
                    lock_end_index
                ):
                    return True
    return False
