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
        
        for i in range(n):
            print()
            for j in range(m):
                print(visited[i][j], end=' ')
        if x == m-1 and y == n-1:
            if all(visited[y][x]):
                print(min(visited[y][x]))
            else:
                print(max(visited[y][x]))
            return

        for dx,dy in dxdy:
            if 0 <= (x+dx) < m and 0 <= (y+dy) < n: # 기본조건(주어진 배열크기를 벗어나지 않아야함)
                
                # 해당 위치가 1) 벽부숨없이 진행한 경로 2) 벽부수고 진행한 경로 에 공통으로 속한 위치라면
                if all(visited[y][x]): 
                    # 1) 벽부숨없이 진행한 경로의 경우
                    # 길은 큐에 추가
                    if is_wall[y+dy][x+dx] == 0 and visited[y+dy][x+dx][0] == 0: 
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][0] = visited[y][x][0] + 1
                    # 벽도 큐에 추가(뿌시기)하고 벽부순 배열에 방문체크
                    elif is_wall[y+dy][x+dx] == 1 and visited[y+dy][x+dx][0] == 0: 
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][1] = visited[y][x][0] + 1
                    
                    # 2) 벽부수고 진행한 경로의 경우
                    # 길만 큐에 추가
                    if is_wall[y+dy][x+dx] == 0 and visited[y+dy][x+dx][1] == 0: 
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][1] = visited[y][x][1] + 1 
                
                # 해당 위치가 1) 벽부숨없이 진행한 경로에 속한다면
                elif visited[y][x][0] != 0: 
                    # 길은 큐에 추가
                    if is_wall[y+dy][x+dx] == 0 and visited[y+dy][x+dx][0] == 0: 
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][0] = visited[y][x][0] + 1
                    # 벽도 큐에추가하고 벽부순 배열에 방문 체크
                    elif is_wall[y+dy][x+dx] == 1 and visited[y+dy][x+dx][0] == 0: 
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][1] = visited[y][x][0] + 1

                # 해당 위치가 2) 벽부수고 진행한 경로에 속한다면
                else: 
                    # 길만 큐에 추가하고 방문체크는 역시 벽부순 배열에 진행
                    if is_wall[y+dy][x+dx] == 0 and visited[y+dy][x+dx][1] == 0:
                        q.append((x+dx,y+dy))
                        visited[y+dy][x+dx][1] = visited[y][x][1] + 1 
        print('!!!',(y,x))
    print(-1)
    return


if __name__ == "__main__":
    n,m = tuple(map(int, sys.stdin.readline().split()))
    is_wall = [] # 0: 이동가능 지점, 1: 벽 을 의미
    for _ in range(n):
        is_wall.append(list(map(int,list(sys.stdin.readline()[:-1]))))
    
    bfs(is_wall)
