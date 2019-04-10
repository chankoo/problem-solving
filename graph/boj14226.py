# https://www.acmicpc.net/problem/14226

# sol
# 화면에 보이는 이모티콘 개수 d와 클립보드에 저장된 이모티콘 개수 c의 튜플 (d, c)를 기본 자료구조로 사용한다 
# d==s이면 소요시간을 출력하고 종료한다
# 이를 위해 bfs로 최단시간에 목표를 달성하는 3가지 연산의 수행 경로를 찾는다
# 즉, 큐에 3가지 연산의 결과인 [(d,d), (d+c,c), (d-1,c)] 를 넣고 소요시간으로 방문체크를 한다
# 방문체크를 위한 이차원 배열 visited[D][C] 를 이용한다
# 큐에서 현재 상태 (d,c)를 뽑았을때 
# visited[next_d][next_c] == 0 이면 (다음점을 방문안했으면)
# visited[next_d][next_c] = visited[d][c] + 1 로 소요시간을 측정한다

import sys
from collections import deque

def bfs(s):
    visited = [[0 for _ in range(2*s+1)] for _ in range(2*s+1)] # 

    q = deque([])
    q.append((1,1))
    visited[1][1] = 1

    while len(q) > 0:
        d, c = q.popleft()

        if d == s:
            print(visited[d][c])
            return

        for n_d, n_c in [(d,d), (d+c,c), (d-1,c)]:
            if 0 < n_d < 2*s+1 and 0 < n_c < 2*s+1 and visited[n_d][n_c] == 0:
                q.append((n_d,n_c))
                visited[n_d][n_c] = visited[d][c] + 1

if __name__ == "__main__":
    s = int(input())
    bfs(s)

