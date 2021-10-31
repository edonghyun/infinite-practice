'''
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

'''

import copy
import itertools

delta_x = [1, 0, -1, 0,]
delta_y = [0, 1, 0, -1,]

def print_board(board):
    for row in board:
        print(row)
    print()

def bfs(copied_map, visited, start_position, width, height):
    q = [start_position]

    while q:
        position = q.pop(0)
        for _ in range(4):
            try:
                x = position[0] + delta_x[_]
                y = position[1] + delta_y[_]

                if x > height or y > width or x < 0 or y < 0:
                    continue

                if visited[x][y]:
                    continue

                if copied_map[x][y] == 0:
                    q.append((x, y))
                    visited[x][y] = True
                    copied_map[x][y] = 2

            except IndexError:
                continue
    
if __name__ == '__main__':
    with open('14502.txt') as f:
        inputs = [
            i.strip() for i in f.readlines()
        ]
        tiles = inputs.pop(0).split(' ')
        height = int(tiles.pop(0))
        width = int(tiles.pop(0))
        
        map = []
        zero_places = []
        for h in range(height):
            map.append([])
            row = inputs.pop(0).split(' ')
            for index, col in enumerate(row):
                value = int(col)
                map[h].append(value)
                if value == 0:
                    zero_places.append((h, index))

        result = -1
        for seperators in itertools.combinations(zero_places, 3):
            copied_map = copy.deepcopy(map)
            for x, y in seperators:
                copied_map[x][y] = 1
            
            visited = [
                [False for _ in range(width)]
                for _ in range(height)
            ]
            for i in range(height):
                for j in range(width):
                    if visited[i][j]:
                        continue

                    if copied_map[i][j] == 2:
                        visited[i][j] = True
                        bfs(copied_map, visited, (i,j), width, height)
            total = 0
            for row in copied_map:
                for col in row:
                    if col == 0:
                        total += 1

            result = max(
                result,
                total,
            )            

        print(result)
