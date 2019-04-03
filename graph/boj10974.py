# https://www.acmicpc.net/problem/10974

# sol
# 경우의 수가 8! 이하이기에 dfs로 풀이 가능
# 일반적인 dfs처럼 visited 배열을 만들고
# 전역변수 path 배열에 다음위치와 현재위치를 저장한다(path[next_idx] = path[idx])
# path는 역추적하여 출력하기위한 배열
# 모든 숫자 방문을 완료할 때마다 path를 출력한다

import sys
import copy

def print_path(i, path): # backtracking the (completed) path list print out numbers
    path_backward = [i,] # 뒤집힌 path 리스트를 저장
    while True:
        i = path[i] # backtrack
        if i == -1: # backtracking 이 끝났음을 의미
            break
        path_backward.append(i) # 거슬러 올라갈 인덱스를 저장
    
    # 다시 뒤집어서 원래 순서대로 출력
    print(' '.join(list(map(lambda x:str(x+1), path_backward[::-1]))))

def dfs(i, visited, path):
    if all(visited):
        print_path(i, path)

    for n_i in range(len(visited)):
        if visited[n_i] == 0:
            visited[n_i] = 1
            path[n_i] = i
            dfs(n_i, visited, path)
            visited[n_i] = 0


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    for i in range(n):
        visited = [0 for _ in range(n)]
        visited[i] = 1
        path = [-1 for _ in range(n)]
        dfs(i, visited, path)