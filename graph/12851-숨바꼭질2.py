# https://www.acmicpc.net/problem/12851

# sol
# 존재하는 최단거리탐색 경로의 개수를 모두 찾아야한다
# 그래서 일반적인 bfs와 다르게 중복으로 탐색 가능하게 만든다
# 또한 그렇기에 visited에 현재 탐색시간을 선형적으로 저장했던 테크닉을 이용할 수 없다
# 문제를 풀려면 위치에 도달하는 시간과 case의 수를 모두 기록해야한다(DP 같은 느낌)
# 또한 현재 위치에서  1)다음 방문 위치가 첫 방문인 경우와
# 2) 첫 방문이 아니지만 다음 위치에 도달하는 시간이 저장된 시간과 같은 경우를 모두 계산에 넣어야 한다
## 어려운 문제.. 완전히 이해하지는 못했다
## https://hello70825.tistory.com/62 코드를 많이 참고했다
## 현재 알고리즘이 틀림

from collections import deque
Max = 100001

def bfs(n,k):
    global Max
    visited_mintime = [Max for _ in range(Max)] # 위치에 도달하는 가장 짧은 시간을 담을 배열
    visited_case_cnt = [0 for _ in range(Max)] # 해당 위치에 mintime에 도달하는 case의 개수 담을 배열

    q = deque([])
    
    q.append(n)
    visited_mintime[n] = 0 # n을 방문하고 (현재시간+1)을 마킹
    visited_case_cnt[n] = 1 # n을 방문하는 첫번째 case임을 기록

    while len(q) > 0:
        # q에서 pop 
        loc = q.popleft()
        # print(loc, end=' ')
        for n_loc in [loc+1, loc-1, loc*2]:
            if 0<=n_loc<Max:
                
                # 1) n_loc에 첫방문
                if visited_mintime[n_loc] == Max: 
                    q.append(n_loc)
                    visited_mintime[n_loc] = visited_mintime[loc] + 1
                    visited_case_cnt[n_loc] = visited_case_cnt[loc] # 현재 loc과 동일한 개수의 case
                
                # 2) n_loc에 첫방문 아니지만 동일한 시간에 방문
                elif (visited_mintime[n_loc] != Max) and (visited_mintime[n_loc] == visited_mintime[loc] + 1):
                    q.append(n_loc)
                    visited_case_cnt[n_loc] = visited_case_cnt[loc] + 1 # 현재 loc의 case보다 하나 많아짐
                    
    print(visited_mintime[k]) # k에 도달하는 최소탐색시간 출력
    print(visited_case_cnt[k]) # k에 도달하는 최소시간탐색인 case 개수 출력


if __name__ == "__main__":
    n,k = tuple(map(int,input().split()))
    bfs(n,k)

