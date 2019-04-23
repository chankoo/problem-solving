# https://www.acmicpc.net/problem/3055

# sol
# bfs_flooding으로 물이 범람하는 시간을 기록해둔다(water_map)
# 그 시간을 조건으로 bfs_dotch를 돌려 고슴도치를 이동시킨다

import sys
from queue import PriorityQueue
from collections import deque

MAX = 987654321

def bfs_flooding():
    global Map, R, C, water

    water_map = [[MAX for _ in range(C)] for _ in range(R)]
    q = PriorityQueue()
    for (r,c) in water:
        q.put((0,r,c))
        water_map[r][c] = 0

    while not q.empty():
        time,r,c = q.get()

        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            n_r = r+dr; n_c = c+dc

            if 0<=n_r<R and 0<=n_c<C and water_map[n_r][n_c]==MAX and Map[n_r][n_c] not in ['X','D']:
                q.put((time+1,n_r,n_c))
                water_map[n_r][n_c] = time+1

    return water_map

def bfs_dotch(water_map): # 고슴도치의 이동
    global Map, R, C, S, D

    visited = [[0 for _ in range(C)] for _ in range(R)]
    q = deque()
    visited[S[0]][S[1]] = 1
    q.append((0,S[0],S[1]))

    while len(q) > 0:
        time, r, c = q.popleft()

        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            n_r = r+dr; n_c = c+dc

            if 0<=n_r<R and 0<=n_c<C:
                if visited[n_r][n_c]==0 and time+1 < water_map[n_r][n_c] and Map[n_r][n_c] != 'X':
                    q.append((time+1,n_r,n_c))
                    visited[n_r][n_c] = 1
                    
                    if Map[n_r][n_c] == 'D':
                        return time+1
    return 'KAKTUS'


if __name__ == "__main__":
    R,C = tuple(map(int, sys.stdin.readline().rstrip('\n').split()))
    
    Map = [[None for _ in range(C)] for _ in range(R)]
    water = []
    S = None # 도치의 초기위치
    D = None # 비버의 집
    for r in range(R):
        for c,val in enumerate(list(sys.stdin.readline().rstrip('\n'))):
            Map[r][c] = val
            if val == '*':
                water.append((r,c))
            elif val == 'S':
                S = (r,c)
            elif val == 'D':
                D = (r,c)

    water_map = bfs_flooding()
    print(bfs_dotch(water_map))