# https://www.acmicpc.net/problem/2667

import sys

def dfs(r, c):
    global Map, N

    for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
        n_r = r + dr; n_c = c + dc

        if 0 <= n_r < N and 0 <= n_c < N:
            if Map[n_r][n_c] == 1:
                Map[n_r][n_c] = -1
                danzi[-1] += 1
                dfs(n_r, n_c)

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip('\n'))
    
    Map = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j, val in enumerate(list(map(int, sys.stdin.readline().rstrip('\n')))):
            Map[i][j] = val

    danzi = []
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 1:
                danzi.append(1)
                Map[i][j] = -1
                dfs(i, j)

    print(len(danzi))
    for cnt in sorted(danzi):
        print(cnt)

