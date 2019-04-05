# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

def bfs(maze):
    q = deque([])
    n = len(maze); m = len(maze[0])
    visited = [[0]*m for _ in range(n)]
    
    q.append((0,0))
    visited[0][0] = 1

    while len(q) > 0:
        loc = q.popleft()
        if loc == (n-1, m-1):
            print(visited[n-1][m-1])
            return 

        for n_loc in [(loc[0],loc[1]+1), (loc[0]+1,loc[1]), (loc[0],loc[1]-1), (loc[0]-1,loc[1])]:
            if 0 <= n_loc[0] < n and 0 <= n_loc[1] < m and visited[n_loc[0]][n_loc[1]] == 0 and maze[n_loc[0]][n_loc[1]] == 1:
                q.append(n_loc)
                visited[n_loc[0]][n_loc[1]] = visited[loc[0]][loc[1]] + 1

if __name__ == "__main__":
    n, m = tuple(map(int, sys.stdin.readline().split()))
    maze = []
    for _ in range(n):
        maze.append(list(map(int, list(sys.stdin.readline())[:-1] )))
    
    bfs(maze)