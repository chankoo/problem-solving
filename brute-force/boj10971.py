# https://www.acmicpc.net/problem/10971

# sol
# N <= 10 이므로 dfs로 풀어버리자

import sys

def input_adjmat(n):
    adjmat = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        adjmat.append(row)
    return adjmat

def dfs(i, cnt, visited, cost):
    global adjmat, min_cost, start

    if cnt == len(adjmat):
        if adjmat[i][start] != 0:
            min_cost = min(min_cost, cost+adjmat[i][start])
        return
    
    if cost >= min_cost:
        return

    for n_i in range(len(adjmat)):
        if adjmat[i][n_i] == 0 or visited[n_i]:
            continue
        visited[n_i] = 1
        dfs(n_i, cnt+1, visited, cost+adjmat[i][n_i])
        visited[n_i] = 0


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    adjmat = input_adjmat(n)
    min_cost = 987654321

    for i in range(n):
        visited = [0 for _ in range(n)]
        visited[i] = 1
        start = i
        dfs(i, 1, visited, 0)

    print(min_cost)
