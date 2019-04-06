# https://www.acmicpc.net/problem/6603

import sys
import copy

def backtrack_path(num, visited):
    global s
    i = s.index(num)

    path_backward = []
    path_backward.append(num)

    while True:
        i = visited[i]
        if i == -1:
            print(' '.join(list(map(str, path_backward[::-1]))))
            return
        path_backward.append(s[i])
    
def dfs(num, cnt, visited):
    global s
    i = s.index(num)

    if cnt == 6:
        backtrack_path(num, visited)
        return 
    
    for n_i, n_num in enumerate(s):
        if num < n_num and visited[n_i] == -1:
            cp_visited = copy.deepcopy(visited)
            cp_visited[n_i] = i
            dfs(n_num, cnt+1, cp_visited)


if __name__ == "__main__":
    cases = []
    while True:
        k, *s = list(map(int, sys.stdin.readline().rstrip('\n').split()))
        if k == 0:
            break
        cases.append(s)
    
    for s in cases:
        for idx, start in enumerate(s):
            visited = [-1 for _ in s]
            if (len(s) - 6) < idx:
                break
            dfs(start, 1, visited)
        if s == cases[-1]:
            break
        print()