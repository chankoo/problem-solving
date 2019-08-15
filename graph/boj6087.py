# https://www.acmicpc.net/problem/6087

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

def is_visited(h, w, di):
    return visited[h][w][di]

def append_new_info(prev_di, di, h, w, prev_mirror_cnt):
    global mirror_cnt_found

    if prev_mirror_cnt >= mirror_cnt_found:
        return

    if prev_di == di:
        mirror_cnt = prev_mirror_cnt
    else:
        mirror_cnt = prev_mirror_cnt+1

    q.append(Info(h, w, di, mirror_cnt))
    

def bfs():
    global q, visited
    dhs = [0,0,1,-1]
    dws = [1,-1,0,0]
    

    C0 = cc_loc[0]
    q.append(Info(C0[0], C0[1], -1, 0 ))

    # Don't visit start point C0 again
    visited[C0[0]][C0[1]][0] = 1
    visited[C0[0]][C0[1]][1] = 1
    visited[C0[0]][C0[1]][2] = 1
    visited[C0[0]][C0[1]][3] = 1  

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
            
            if is_visited(n_h, n_w, n_di):
                continue

            append_new_info(cur_di, n_di, n_h, n_w, cur_mirror_cnt)
            if (n_h, n_w) in cc_loc:
                mirror_cnt_found = q[-1].mirror_cnt
            visited[n_h][n_w][n_di] = 1
            
    return mirror_cnt_found-1  # subtract for starting point

if __name__=="__main__":
    W, H = tuple(map(int, sys.stdin.readline().split()))

    Map = []
    cc_loc = []
    wall_loc = []
    for h in range(H):
        this_line = list(sys.stdin.readline())
        Map.append(this_line)
        for w, char in enumerate(this_line):
            if char=='C':
                cc_loc.append((h,w))
            elif char=='*':
                wall_loc.append((h,w))
    
    q = deque()
    visited = [[[0 for _ in range(4)] for _ in range(W)] for _ in range(H)]  # 3-dim array: h, w, di
    mirror_cnt_found = 987654321
    print(bfs())