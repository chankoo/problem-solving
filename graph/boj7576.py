# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

def bfs(unripe):
    global ripe_tom, box, m,n

    if unripe == 0:
        return 0

    q = deque()
    for (r,c) in ripe_tom:
        q.append((0,r,c))
    
    while len(q) > 0:
        day,r,c = q.popleft()  # 큐에 있는 익은 토마토 중 최소 일수인 토마토의 값을 pop

        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:  
            n_r = r+dr; n_c = c+dc
            if 0 <= n_r < m and 0 <= n_c < n and box[n_r][n_c] == 0:
                q.append((day+1, n_r,n_c))  # 해당 토마토에 영향 받아 익는 토마토 역시 최소 일수이다
                box[n_r][n_c] = day+1
                unripe -= 1
                
                if unripe == 0:
                    return day+1
    return -1


if __name__ == "__main__":
    n,m = tuple(map(int, sys.stdin.readline().rstrip('\n').split()))
    
    box = []
    ripe_tom = []
    unripe = 0
    for r in range(m):
        box.append(list(map(int, sys.stdin.readline().split())))
        for c, val in enumerate(box[-1]):
            if val == 1:
                ripe_tom.append((r,c))
            elif val ==0:
                unripe += 1

    print(bfs(unripe))