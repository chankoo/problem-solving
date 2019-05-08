# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

def bfs():
    global ripes, unripes, h, n, m
    if unripes == 0:
        return 0

    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]    
    q = deque()
    dds = [-1,0,0,0,0,1]
    drs = [0,1,0,-1,0,0]
    dcs = [0,0,1,0,-1,0]

    for ripe in ripes:
        q.append(ripe)
        visited[ripe[0]][ripe[1]][ripe[2]] = True

    while len(q) > 0:
        d,r,c,day = q.popleft()

        for dd,dr,dc in zip(dds,drs,dcs):
            n_d = d+dd; n_r = r+dr; n_c = c+dc

            if 0<=n_d<h and 0<=n_r<n and 0<=n_c<m:
                if not visited[n_d][n_r][n_c] and box[n_d][n_r][n_c] == 0:
                    q.append((n_d,n_r,n_c,day+1))
                    visited[n_d][n_r][n_c] = True
                    unripes -= 1
                    if unripes == 0:
                        return day+1
    return -1


if __name__ == "__main__":
    m,n,h = tuple(map(int, sys.stdin.readline().rstrip('\n').split()))
    
    box = [[[None for _ in range(m)] for _ in range(n)] for _ in range(h)]
    ripes = []
    unripes = 0
    for d in range(h):
        for r in range(n):
            for c, val in enumerate(tuple(map(int, sys.stdin.readline().rstrip('\n').split()))):
                box[d][r][c] = val
                if val == 1:
                    ripes.append((d,r,c,0))
                elif val == 0:
                    unripes += 1
    print(bfs())
