# https://www.acmicpc.net/problem/1260

# solution
# 1) 주어진 입력을 인접행렬로 저장한다
# 2) 현재 정점 그때그때 출력하는 dfs를 돌린다
# 3) bfs 하고 path를 출력한다

# TIL
# adj_mat = [([0,] * n),]*n -> 이런식으로 초기화 하면안됨. copy라 원소의 id값 다 같아지는 문제
# 파이썬 입력으로 input()은 굉장히 느리다. sys.stdin.readline() 사용
# dfs의 경우 최단거리 찾는 문제(탐색 여러번 반복)와 단순히 탐색하는 문제(한번만 탐색) 구분해서 풀자
## 최단거리 찾는 경우만 여러번 반복해야해서 visited 리셋필요
# 반면 bfs의 path는 그 자체로 최단거리(자체적으로 여러개 path로 탐색)

# bfs 제대로 이해하자
## 1) bfs는 재귀없이 반복만
## 2) 방문과 발견 시점의 분리
## 3) 큐에 중복된 정점 안들어가게 조심
## 4) 정점 방문 표시는 반드시 큐에 넣을때 해야함

from collections import deque
import sys

def dfs(v):
    global adj_mat, visited
    
    print(v+1, end=' ')

    for n_v, is_conn in enumerate(adj_mat[v]): # 다음으로 방문할 next_v를 찾기위해 인접행렬의 v번째 row 순회한다
        if v == n_v:continue # 같은 v에 대해선 탐색하지 않음
        if is_conn == 1 and visited[n_v] == 0: # 현재 v와 연결된 next_v에 방문하지 않았으면 방문한다
            visited[n_v] = 1 # next_v에 방문했음을 마킹
            dfs(n_v)
        


def bfs(start):
    global adj_mat

    visited = [0 for _ in range(n)]
    path = deque([])

    q = deque([start,]) # 첫 정점 q에 push하며 시작
    visited[start] = 1 # q에 push 순간 방문표시

    while len(q) > 0:
        # 방문(q에서 pop하는 일)
        v = q.popleft()
        path.append(v)
        
        # 발견(q에 push하는 일)
        for n_v,is_conn in enumerate(adj_mat[v]):# 방문할 next_v를 찾기위해 인접행렬의 v번째 row 순회한다
            if v == n_v: continue # 같은 v에 대해선 탐색하지 않음
            if is_conn == 1 and visited[n_v] == 0: # v 다음에 방문할수있고, 현재 q에 없는 next_v 있으면
                q.append(n_v) # 발견한 next_v를 큐에 추가
                visited[n_v] = 1 # q에 push 순간 방문표시

    for v in path:
        print(v+1, end=' ')



if __name__ == "__main__":
    n,m,v = tuple(map(int,sys.stdin.readline().split()))
    v = v-1 # 인덱스로 탐색위해 정점 번호를 하나 줄여준다(v가 1부터 시작하기 때문)
    
    # 인접행렬 초기화 및 저장
    adj_mat = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        r,c = tuple(map(int,sys.stdin.readline().split()))
        adj_mat[r-1][c-1] = 1
        adj_mat[c-1][r-1] = 1
    
    # dfs
    visited = [0 for _ in range(n)]
    visited[v] = 1
    dfs(v)

    print('\n',end='')

    # bfs
    bfs(v)


