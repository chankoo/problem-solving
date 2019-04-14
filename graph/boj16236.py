# https://www.acmicpc.net/problem/16236

# sol
# 상어객체를 구현하여 bfs로 최단거리의 가능한 먹이를 탐색한다
# 먹이의 딕셔너리(fish_dic)에 대해서
# 1) bfs하며 최단거리이면서 (여럿일 경우 위쪽/왼쪽순) 먹을 수 있는(상어보다 사이즈 작은) 먹이 탐색
#   1-1) 이때 가능한 먹이가 여럿일 수 있기에 bfs 큐에 상어 이동거리를 포함하는 변형이 들어간다
#   1-2) 가능한 먹이가 없으면 그때까지 상어 이동거리를 return하고 끝낸다 
# 2) 결정된 먹이를 먹고 상어의 상태와 space를 업데이트 한다
# 3) 가능한 먹이 없을때까지 bfs를 반복한다  

import sys
from collections import deque
from queue import PriorityQueue

MAX = 987654321

class Shark:
    size = 2
    food_cnt = 0
    r = None; c = None
    total_time = 0

    def __init__(self, r=None, c=None):
        self.r = r
        self.c = c

    def _size_up(self):
        self.size += 1
    
    def food_cnt_up(self):
        self.food_cnt += 1
        if self.food_cnt == self.size:
            self._size_up()
            self.food_cnt = 0

    def set_loc(self, r, c):
        self.r = r
        self.c = c

    def plus_total(self, time):
        self.total_time += time


def bfs_find_fish(shark)->tuple:
    global space
    visited = [[0 for _ in range(n)] for _ in range(n)]

    bfs_q = PriorityQueue()
    bfs_q.put( (0, shark.r,shark.c) )
    visited[shark.r][shark.c] = 1
    
    min_dist = MAX
    target_loc = tuple()
    while not bfs_q.empty():
        d,r,c = bfs_q.get() # 가까운거리 우선으로 현재 위치를 get한다

        if d >= min_dist: # 뽑혀져나온 지점까지 이동거리가 최단거리 이상이라면 더이상의 탐색은 무의미하다
            break

        move = [(-1,0), (0,-1), (1,0), (0,1)]
        for dr,dc in move:
            n_d, n_r, n_c = (d+1, r+dr, c+dc)
            if 0 <= n_r < n and 0 <= n_c < n:
                if space[n_r][n_c]!=0 and space[n_r][n_c] < shark.size and n_d < min_dist: # 최단거리 먹이를 찾은 경우 탐색결과 업데이트
                    visited[n_r][n_c] = 1
                    target_loc = (n_r, n_c)
                    min_dist = n_d
                elif space[n_r][n_c]!=0 and space[n_r][n_c] < shark.size and n_d == min_dist: # 현재 최단거리인 먹이까지와 이동거리 같다면 위치를 따진다
                    visited[n_r][n_c] = 1
                    if n_r < target_loc[0]: # 높이가 더 위라면
                        target_loc = (n_r, n_c)
                        min_dist = n_d
                    elif n_r == target_loc[0] and n_c < target_loc[1]: # 높이 같을때 더 왼쪽에 있으면
                        target_loc = (n_r, n_c)
                        min_dist = n_d
                    else:
                        continue
                elif (space[n_r][n_c]==0 or space[n_r][n_c] == shark.size) and visited[n_r][n_c] == 0: # 이동만 가능한 경우
                    visited[n_r][n_c] = 1
                    bfs_q.put((n_d,n_r,n_c))
    
    if target_loc == tuple():
        return MAX, (None, None)
    return min_dist, target_loc

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    space = []
    fish_dic = {}
    shark = Shark()
    
    for r in range(n):
        row = list(map(int, sys.stdin.readline().rstrip('\n').split()))
        space.append(row)
        for c, val in enumerate(row):
            if val == 9:
                shark.set_loc(r, c)
            elif val != 0:
                fish_dic[(r, c)] = val

    while len(fish_dic) > 0:
        # 먹이 탐색
        min_dist, target_loc = bfs_find_fish(shark)
        if min_dist == MAX:
            break

        # 상어의 이동과 상태변화, 그리고 fish_dic의 조정
        space[shark.r][shark.c] = 0 
        shark.set_loc(target_loc[0],target_loc[1])
        shark.food_cnt_up()
        space[target_loc[0]][target_loc[1]] = 0
        shark.plus_total(min_dist)
        del fish_dic[(target_loc[0],target_loc[1])]

    print(shark.total_time)

