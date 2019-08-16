# https://www.acmicpc.net/problem/6087

# sol
# 1) 약간의 테크닉이 필요한 BFS 문제이다
# 2) 방문체크시 direction을 변수로 넣는 것이 핵심이기에 3차원의 visited 배열을 이용했다
#     2-0) 즉 visited 배열은 height, width, direction(0,1,2,3)의 차원이다
#     2-1) visited의 element는 mirror_cnt를 의미한다
#     2-2) 현재 mirror_cnt가 visited 배열의 해당 위치에 저장된 mirror_cnt 값 보다 적을때를 valid_visit으로 인정한다
# 3) 마지막으로 C_end(통신의 목표인 레이저)의 mirror_cnt 중 0이 아닌 최소값을 리턴한다

import sys
from collections import deque

class Info:
    def __init__(self, h, w, di, mirror_cnt):
        self.h = h
        self.w = w
        self.di = di
        self.mirror_cnt = mirror_cnt

    def get_info(self):
        return self.h, self.w, self.di, self.mirror_cnt


def is_wall(h, w):
    return (h, w) in wall_loc

def is_in_the_map(h, w):
    return 0<=h<H and 0<=w<W

def is_valid_visited(n_h, n_w, n_di, cur_mirror_cnt):
    if visited[n_h][n_w][n_di] == 0:
        return True
    elif visited[n_h][n_w][n_di] > cur_mirror_cnt:
        return True
    else:    
        return False
        
def append_new_info(cur_di, n_di, n_h, n_w, cur_mirror_cnt):
    if cur_di == n_di:
        mirror_cnt = cur_mirror_cnt
    else:
        mirror_cnt = cur_mirror_cnt+1

    q.append(Info(n_h, n_w, n_di, mirror_cnt))
    visited[n_h][n_w][n_di] = mirror_cnt

def get_final_mirror_cnt(C_end):
    final_mirror_cnt = 987654321
    for cnt in visited[C_end[0]][C_end[1]]:
        if cnt < final_mirror_cnt and cnt != 0:
            final_mirror_cnt = cnt
    return final_mirror_cnt-1  # subtract for starting point

def bfs():
    global q, visited, cc_loc, wall_loc
    dhs = [0,0,1,-1]
    dws = [1,-1,0,0]

    C_start = cc_loc[0]
    C_end = cc_loc[1]
    q.append(Info(C_start[0], C_start[1], -1, 0 ))

    # starting point visited check
    visited[C_start[0]][C_start[1]][0] = 1
    visited[C_start[0]][C_start[1]][1] = 1
    visited[C_start[0]][C_start[1]][2] = 1
    visited[C_start[0]][C_start[1]][3] = 1  

    while len(q) > 0:
        info = q.popleft()
        cur_h, cur_w, cur_di, cur_mirror_cnt = info.get_info()

        for n_di in [0,1,2,3]:  # right, left, down, up
            n_h = cur_h + dhs[n_di]
            n_w = cur_w + dws[n_di]

            if not is_in_the_map(n_h, n_w):
                continue
            if is_wall(n_h, n_w):
                continue
            if is_valid_visited(n_h, n_w, n_di, cur_mirror_cnt):
                append_new_info(cur_di, n_di, n_h, n_w, cur_mirror_cnt)
            
    return get_final_mirror_cnt(C_end)

if __name__=="__main__":
    W, H = tuple(map(int, sys.stdin.readline().split()))

    cc_loc = []
    wall_loc = []
    for h in range(H):
        this_line = list(sys.stdin.readline())
        for w, char in enumerate(this_line):
            if char=='C':
                cc_loc.append((h,w))
            elif char=='*':
                wall_loc.append((h,w))
    
    q = deque()
    visited = [[[0 for _ in range(4)] for _ in range(W)] for _ in range(H)]  # 3-dim array: h, w, di
    print(bfs())