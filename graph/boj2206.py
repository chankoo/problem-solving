# https://www.acmicpc.net/problem/2206

# sol
# 벽을 부술수있는 모든 경우에 대해 bfs 돌리려했으나 시간초과
# bfs 도중에 벽을 부수는 정보를 관리해야한다
# 방문체크를 위한 visited 배열에 두가지 정보를 기록하는 것이 핵심
# 벽을 부수는 이벤트가 발생한 경로와 그렇지 않은 경로는 아예 다른 것이기 때문이다

import sys
from collections import deque

def bfs(is_wall):
    visited = [[[0,0] for _ in range(m)] for _ in range(n)]

    dxdy = [(0,1),(1,0),(-1,0),(0,-1)]
    q = deque([])
    q.append((0,0))
    visited[0][0] = [1,0]

    while len(q) > 0:
        x, y = q.popleft()

        if x == m-1 and y == n-1:
            if all(visited[y][x]):
                print(min(visited[y][x]))
            else:
                print(max(visited[y][x]))
            return

        for dx,dy in dxdy:
            if 0 <= (x+dx) < m and 0 <= (y+dy) < n: # 기본조건(주어진 배열크기를 벗어나지 않아야함)
                
                if all(visited[y][x]): # 해당 위치가 1) 벽부숨없이 진행한 경로 2) 벽부수고 진행한 경로 에 공통으로 속한 위치라면
                    # 1) 벽부숨없이 진행한 경로의 경우
                    if is_wall[y+dy][x+dx] == 0 and visited[y+dy][x+dx][0] == 0: # 벽이 아닌 지점은 큐에 추가
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][0] = visited[y][x][0] + 1
                    elif is_wall[y+dy][x+dx] == 1 and visited[y+dy][x+dx][0] == 0: # 벽을 만난 경우 부수고 벽이있던 자리로 이동
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][1] = visited[y][x][0] + 1
                    
                    # 2) 벽부수고 진행한 경로의 경우
                    if is_wall[y+dy][x+dx] == 0 and visited[y+dy][x+dx][1] == 0: # 벽이 아닌 지점만 큐에 추가
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][1] = visited[y][x][1] + 1 
                
                elif visited[y][x][0] != 0: # 해당 위치가 1) 벽부숨없이 진행한 경로에 속한다면
                    if is_wall[y+dy][x+dx] == 0 and visited[y+dy][x+dx][0] == 0: # 벽이 아닌 지점
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][0] = visited[y][x][0] + 1
                    elif is_wall[y+dy][x+dx] == 1 and visited[y+dy][x+dx][0] == 0: # 벽을 만난 경우 부수고 벽이있던 자리로 이동
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][1] = visited[y][x][0] + 1

                else: # 해당 위치가 2) 벽부수고 진행한 경로에 속한다면
                    if is_wall[y+dy][x+dx] == 0 and visited[y+dy][x+dx][1] == 0: # 벽이 아닌 지점
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][1] = visited[y][x][1] + 1 
    print(-1)
    return


if __name__ == "__main__":
    n,m = tuple(map(int, sys.stdin.readline().split()))
    is_wall = [] # 0: 이동가능 지점, 1: 벽 을 의미
    for _ in range(n):
        is_wall.append(list(map(int,list(sys.stdin.readline()[:-1]))))
    
    bfs(is_wall)
