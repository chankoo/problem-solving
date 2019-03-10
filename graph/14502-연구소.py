# https://www.acmicpc.net/problem/14502

# solution

# 1) 임의로 3개의 벽을 세운다(dfs)
# 2) 바이러스를 퍼뜨린다(bfs)
# 3) 안전구역의 크기를 구해서 최대값을 갱신한다
# 4) 1)로 돌아가 모든 경우에 대해 반복한다
# 5) 안전구역 크기의 최대값을 출력한다

# TIL
# 2차원 배열에서 가능한 모든 조합을 재귀적으로 탐색하는 코드( line:60~66 )
## -> 몫(i//m)과 나머지(i%m)를 이용한 탐색과 재귀함수 내에 반복문 있는 형태 

import copy
from collections import deque


def calc_safe_area():
    global walled_map
    
    area = 0
    for i in range(N):
        for j in range(M):
            if walled_map[i][j] == 0:
                area += 1
    return area


def virus_spread(virus_lst_copy): # 초기의 virus_lst를 받아서 bfs로 virus 퍼뜨림
    global walled_map
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    q = deque(virus_lst_copy)
    while len(q) > 0:
        x, y = q.popleft()
        for d_idx in range(4):
            next_x = x + dx[d_idx]
            next_y = y + dy[d_idx]

            if ( (next_x >=0) and (next_x <N) and (next_y >=0) and (next_y <M) and (walled_map[next_x][next_y]==0) ):
                walled_map[next_x][next_y] = 2 
                q.append((next_x,next_y))


def calculate(start, wall_cnt): # 벽을 세운 뒤 바이러스 퍼뜨리고 안전구역 넓이 계산해 최대값일 경우 갱신
    global lab_map, max_area, N, M

    if wall_cnt == 3: # 3개의 벽 모두 세워짐
        global walled_map
        walled_map = copy.deepcopy(lab_map)
        virus_lst_copy = copy.deepcopy(virus_lst)

        virus_spread(virus_lst_copy)

        max_area = max(max_area, calc_safe_area())
        return

    for i in range(start, N*M):
        x = i//M
        y = i%M
        if lab_map[x][y] == 0:
            lab_map[x][y] = 1
            calculate(i+1,wall_cnt+1)
            lab_map[x][y] = 0


if __name__ == "__main__":
    N, M = tuple(map(int, input().split()))

    lab_map = []
    for _ in range(N):
        lab_map.append(list(map(int, input().split())))

    virus_lst = []
    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 2:
                 virus_lst.append((i,j))

    max_area = 0 # 안전구역의 최대크기
    calculate(0,0)
    print(max_area)
