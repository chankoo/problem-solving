# https://www.acmicpc.net/problem/4963

import sys
sys.setrecursionlimit(10**4)

def input_tc():
    global input_flag, visited, W, H

    W,H = tuple(map(int, sys.stdin.readline().rstrip('\n').split()))
    if (W,H) == (0,0):
        input_flag = False
        return None, None
    
    lands = []
    island = [[-1 for _ in range(W)] for _ in range(H)]
    for h in range(H):
        for w,val in enumerate(list(map(int, sys.stdin.readline().rstrip('\n').split()))):
            island[h][w] = val
            if val == 1:
                lands.append((h,w))
    return lands,island

def dfs(h,w):
    global island, visited
    dhs = [1,1,1,0,0,0,-1,-1,-1]
    dws = [1,0,-1,1,0,-1,1,0,-1]

    for dh,dw in zip(dhs, dws):
        n_h = h+dh; n_w = w+dw
        if 0<=n_h<H and 0<=n_w<W and visited[n_h][n_w] == 0 and island[n_h][n_w] == 1:
            visited[n_h][n_w] = 1
            dfs(n_h, n_w)


if __name__ == "__main__":
    input_flag = True
    while True:
        W, H = None, None
        lands, island = input_tc()
        if not input_flag:
            break
        
        cnt_island = 0
        visited = [[0 for _ in range(W)] for _ in range(H)]
        for land in lands:
            h = land[0]; w = land[1]
            if visited[h][w] == 0:
                visited[h][w] = 1
                cnt_island += 1
                dfs(h,w)
        print(cnt_island)
