# https://www.acmicpc.net/problem/1261

# sol
# bfs와 우선순위큐를 이용한다
# 벽을 부순 횟수의 오름차순으로 정렬된 우선순위큐를 이용하면 최소의 벽을 부수는 경로를 먼저 탐색할 수 있다

import sys
from queue import PriorityQueue

def bfs():
    global maze
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    q = PriorityQueue()

    q.put((0, 0,0))
    visited[0][0] = 0
    while not q.empty():
        cnt,r,c = q.get()
        if r == n-1 and c == m-1:
            print(cnt)
            return

        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            n_r = r+dr; n_c = c+dc

            if 0 <= n_r < n and 0<= n_c < m and visited[n_r][n_c] == -1:
                if maze[n_r][n_c] == 0: # 뚫려있음 
                    q.put((cnt,n_r,n_c))
                    visited[n_r][n_c] = cnt

                else: # 벽임
                    q.put((cnt+1,n_r,n_c))
                    visited[n_r][n_c] = cnt + 1


if __name__ == "__main__":
    m,n = tuple(map(int,sys.stdin.readline().strip('\n').split()))
    maze = [] # n by m
    for _ in range(n):
        maze.append(list(map(int,sys.stdin.readline().strip('\n'))))
    bfs()

