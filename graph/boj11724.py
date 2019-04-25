# https://www.acmicpc.net/problem/11724

# sol
# dfs를 이용하여 시작점에서 탐색되는 하나의 연결요소를 카운트한다
# 한 정점이 두개의 연결요소에 속할 수 없으므로 방문체크 후 해제하지 않는다
# edge가 없는 정점도 연결요소로 카운트하며, 파이썬의 경우 재귀 제한에 걸리기에 limit값을 높여준다

import sys
sys.setrecursionlimit(10**4)

def dfs(u):  # search u -> v 
    global adj_lst, n, m, visited

    for v in adj_lst[u]:
        if not visited[v]:
            visited[v] = True
            dfs(v)

if __name__ == "__main__":
    n, m = tuple(map(int, sys.stdin.readline().rstrip().split()))

    adj_lst = dict.fromkeys(range(1,n+1), None)
    for _ in range(m):
        u, v = tuple(map(int, sys.stdin.readline().rstrip().split()))
        
        if adj_lst[u] is not None:
            adj_lst[u].append(v)
        else:
            adj_lst[u] = [v,]
        
        if adj_lst[v] is not None:
            adj_lst[v].append(u)
        else:
            adj_lst[v] = [u,]

    conn_comp_cnt = 0
    visited = [False for _ in range(n+1)]
    for s in range(1, n+1):
        if not visited[s]:
            conn_comp_cnt += 1
            visited[s] = True

            if adj_lst[s] is None:
                continue
            dfs(s)
    print(conn_comp_cnt)