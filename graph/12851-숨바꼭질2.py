# https://www.acmicpc.net/problem/12851

# sol
# 존재하는 최단거리탐색 경로의 개수를 모두 찾아야한다
# 그래서 일반적인 bfs와 다르게 중복으로 탐색 가능하게 만든다
# 또한 그렇기에 visited에 현재 탐색시간을 선형적으로 저장했던 테크닉을 이용할 수 없다
# 문제를 풀려면 위치에 도달하는 시간과 case의 수를 모두 기록해야한다(DP 같은 느낌)
# 또한 현재 위치에서  1) 다음 방문 위치가 첫 방문인 경우와
# 2) 첫 방문이 아니지만 다음 위치에 도달하는 시간이 저장된 시간과 같은 경우를 모두 계산에 넣어야 한다
# case 2) 의 경우는 방문없이 카운트만 필요하기에 큐에 넣지않는다. 방문하면 중복이 생기게 된다

from collections import deque

def bfs(n,k):
    MAX = 100001
    visited = [[0,-1] for _ in range(MAX)] # 해당 위치에 [방문 횟수, 시간]을 기록 
    # visited_mintime = [-1 for _ in range(MAX)] # 위치에 도달하는 가장 짧은 시간을 담을 배열
    # visited_case_cnt = [0 for _ in range(MAX)] # 해당 위치에 mintime에 도달하는 case의 개수 담을 배열

    q = deque()
    
    q.append(n)
    visited[n][0] = 1 # n을 방문하는 첫번째 case임을 기록
    visited[n][1] = 0 # n을 방문하고 현재시간을 마킹

    while len(q) > 0:
        loc = q.popleft()

        for n_loc in [loc+1, loc-1, loc*2]:
            if 0<=n_loc<MAX:
                # 1) n_loc에 첫방문
                if visited[n_loc][1] == -1: 
                    q.append(n_loc)
                    visited[n_loc][1] = visited[loc][1] + 1
                    visited[n_loc][0] = visited[loc][0] # 현재 loc과 동일한 개수의 case
                
                # 2) n_loc에 첫방문 아니지만 동일한 시간에 방문
                elif visited[n_loc][1] == visited[loc][1] + 1:
                    visited[n_loc][0] += visited[loc][0] # n_loc 도달 경로 개수에 현재 경로까지의 case를 더함
                    
    print(visited[k][1]) # k에 도달하는 최소탐색시간 출력
    print(visited[k][0]) # k에 도달하는 최소시간탐색인 case 개수 출력

if __name__ == "__main__":
    n,k = tuple(map(int,input().split()))
    bfs(n,k)