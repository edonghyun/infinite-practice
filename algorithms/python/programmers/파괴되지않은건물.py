def solution(board, skills):
    answer = 0
    r_length = len(board)
    c_length = len(board[0])
    
    board_map = [
        [0 for _ in range(c_length + 1)] 
            for _ in range(r_length + 1)
    ]

    for skill in skills:
        _type, r1, c1, r2, c2, degree = skill
        
        impact_value = -degree if _type == 1 else degree
        board_map[r1][c1] += impact_value
        board_map[r1][c2 + 1] += -impact_value
        
        board_map[r2 + 1][c1] += -impact_value
        board_map[r2 + 1][c2 + 1] += impact_value
        
    for i, row in enumerate(board_map):
        for j, col in enumerate(row):
            if j == 0:
                continue
                
            board_map[i][j] += board_map[i][j-1]

    for i, row in enumerate(board_map):
        if i == 0:
            continue
            
        for j, col in enumerate(row):
            board_map[i][j] += board_map[i-1][j]
                
    for i in range(r_length):
        for j in range(c_length):
            board[i][j] += board_map[i][j]
            if board[i][j] >= 1:
                answer += 1

    return answer