# https://www.acmicpc.net/problem/1260

import copy
from collections import deque
import sys

# solution
# 1) 주어진 입력을 인접행렬로 저장한다
# 2) 현재 경로를 가지고 다니는 dfs를 돌려 경로를 출력한다
# 3) bfs 하고 출력한다

# TIL
# adj_mat = [([0,] * n),]*n -> 이런식으로 초기화 하면안됨. copy라 원소의 id값 다 같아지는 문제
# 파이썬 입력으로 input()은 굉장히 느리다. sys.std
# bfs 제대로 이해하자
## 1) bfs는 재귀없이 반복만
## 2) 방문과 발견 시점의 분리
## 3) 큐에 중복된 정점 안들어가게 조심


def dfs(v,path):
    global adj_mat, visited

    if len(path) == n: # 모든 정점을 방문하면
        for v in path:
            print(v+1, end=' ')
        return

    for n_v, is_conn in enumerate(adj_mat[v]): # 다음으로 방문할 next_v를 찾기위해 인접행렬의 v번째 row 순회한다
        if v == n_v:continue # 같은 v에 대해선 탐색하지 않음
        if is_conn == 1 and visited[n_v] == 0: # 현재 v와 연결된 next_v에 방문하지 않았으면 방문한다
            visited[n_v] = 1 # next_v에 방문했음을 마킹
            path.append(n_v)
            dfs(n_v,path)
            visited[n_v] = 0 # 재귀적 탐색하므로 현재 레벨에선 다시 언마킹


def bfs(start):
    global adj_mat

    visited = [0 for _ in range(n)]
    path = deque([])
    q = deque([start,]) # 첫 정점 q에 push하며 시작

    while len(q) > 0:
        # 방문(q에서 pop하는 일)
        v = q.popleft()
        visited[v] = 1
        path.append(v)
        
        # 발견(q에 push하는 일)
        for n_v,is_conn in enumerate(adj_mat[v]):# 방문할 next_v를 찾기위해 인접행렬의 v번째 row 순회한다
            if v == n_v: continue # 같은 v에 대해선 탐색하지 않음
            if is_conn == 1 and visited[n_v] == 0 and n_v not in q: # v 다음에 방문할수있고 현재 q에 없는 next_v 있으면
                q.append(n_v) # 발견한 next_v를 큐에 추가
                #print(v, '발견 ->',q)
    
    # 경로 출력
    for v in path:
        print(v+1, end=' ')



if __name__ == "__main__":
    n,m,v = tuple(map(int,input().split()))
    v = v-1 # 인덱스로 탐색위해 정점 번호를 하나 줄여준다(v가 1부터 시작하기 때문)
    
    # 인접행렬 초기화 및 저장
    adj_mat = []
    for _ in range(n):
        adj_mat.append([0 for _ in range(n)])

    
    for _ in range(m):
        r,c = tuple(map(int,sys.stdin.readline().split()))
        adj_mat[r-1][c-1] = 1

    # dfs
    visited = [0 for _ in range(n)]
    visited[v] = 1
    path = deque([v,])
    dfs(v,path)

    print('\n',end='')

    # bfs
    bfs(v)


