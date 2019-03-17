# https://www.acmicpc.net/problem/1697

# solution dfs
# 1) 현재위치 n에서 가능한 세가지 경우 +1, -1, *2 를 dfs한다
# 2) 이때 dfs의 depth는 탐색 시간을 의미하기에 depth가 현재 최소탐색시간보다 큰 경우는 탐색하지 않는다
# 3) 모든 탐색이 끝난 후 최소탐색시간을 출력한다
# 한계: 파이썬 재귀 depth의 한계(기본적으로 1000) -> ex) 인풋으로 0 100000 이 들어올 경우 10만번 초과 재귀로 런타임 에러
# 좀더 근본적인 한계: 재귀로 탐색하기에는 너무 큰 범위(0 ~ 100000/ +1, -1)
# 조건을 더 줘서 탐색 범위를 줄여보고자 했으나 여전히 시간초과발생

# solution bfs
# 1) 현재위치 n에서 가능한 세가지 경우 +1, -1, *2 를 bfs한다
# 2-1) 이때 방문 여부를 체크하는 배열(visited)에 몇 번째로 방문하는지 count를 입력한다
# 2-2) 즉, q에 visited[next_loc] = visited[loc] + 1 을 저장한다
# 3) k 위치를 탐색 성공하면 최소탐색시간인 visited[k]를 출력한다

# TIL
# dfs는 최단거리를 구하지 않는다. 최단거리를 구하려면 모든 경우를 탐색해야하는데 백트래킹하더라도 시간초과의 위험이 크다
# 더구나 dfs는 재귀를 이용하기에 문제가 많다
# 최단거리 탐색은 bfs를 이용한다
# bfs에서 방문여부 체크하는 동시에 depth 구하는 테크닉
# dfs든 bfs든 방문여부 체크 꼭 하자

import sys
from collections import deque

# def dfs(n,k,depth):
#     global min_time, visited
#     print(n,depth)
#     # 탐색시간 줄이기 위한 코드(임시방편)
#     if n>2*k: # n이 너무 커지는 경우 탐색에서 제외
#         return
#     if depth >20: # 20초과의 depth는 허용않으므로써 재귀 횟수 제한의 문제와 무한루프 문제는 해결 
#         return

#     if depth >= min_time: # 이미 depth가 현재 탐색최소시간 이상이라 더 이상 탐색이 불필요한 경우
#         return

#     if abs(n-k) == 0: # 탐색성공한경우
#         min_time = depth
#         return

#     if n == 0:
#         if visited[n+1] == 0:
#             visited[n+1] = 1
#             dfs(n+1,k,depth+1)
#             visited[n+1] = 0
    
#     else:
#         if visited[n*2] == 0:
#             visited[n*2] = 1
#             dfs(n*2,k,depth+1)
#             visited[n*2] = 0

#         if visited[n+1] == 0:
#             visited[n+1] = 1
#             dfs(n+1,k,depth+1)
#             visited[n+1] = 0
        
#         if visited[n-1] == 0:
#             visited[n-1] = 1
#             dfs(n-1,k,depth+1)
#             visited[n-1] = 0


def bfs(n,k):
    q = deque([])
    visited = [0 for _ in range(100001)]

    q.append(n)
    visited[n] = 1

    while len(q) > 0:
        loc = q.popleft()

        if loc==k:
            return visited[k] - 1 # k를 방문(검색성공)할때 탐색 횟수
        
        for n_loc in [loc+1, loc*2, loc-1]:
            if (n_loc < 100001) and (n_loc >= 0) and (visited[n_loc] == 0):
                q.append(n_loc)
                visited[n_loc] = visited[loc] + 1

    
if __name__ == "__main__":
    n,k = tuple(map(int,input().split()))

    print(bfs(n,k))





