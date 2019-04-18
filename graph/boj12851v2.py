# https://www.acmicpc.net/problem/12851

# sol v2
# 숨바꼭질2의 solution2 이다
# 정점을 큐에 넣을때가 아니라 큐에서 뺄때 방문체크를 하는 bfs를 이용한다
# 다만 시간체크는 이전 정점의 방문시간에서 +1 해야하므로 큐에 넣을때 해준다
# 당연히 시간체크는 중복 계산하면 안되기에 큐에 넣을때 해주면 된다
# 이렇게하면 큐에 삽입된 같은 정점간의 level(시간)이 다를수있다. level이 다른 정점까지 카운트하면 안되기에 큐에 넣기전 이를 검사한다

# v1은 큐에 넣을때 방문체크를 하며 중복되는 정점은 큐에 넣지 않는 방법이고
# v2는 큐에서 뺄때 중복체크를 하며 중복되는 점까지 큐에 넣는 방법이다
# 그렇기에 v1에서는 방문 카운트를 동적으로 증가시키는 방법을 택했고(큐에 넣는 시점에 현재 정점 방문 카운트를 알고있으므로)
# 반면 v2에서는 방문 카운트를 +1씩 일괄적으로 늘리는 차이가 있다
# 큐에 삽입하는 양이 많으므로 v2의 속도가 더 느리다

from collections import deque

def bfs(n,k):
    MAX = 100001  
    visited = [[0,-1] for _ in range(MAX)] # 해당 위치에 [방문 횟수, 시간]을 기록 
    
    q = deque()
    q.append(n)
    visited[n] = [0,0]

    while len(q) > 0:
        loc = q.popleft()

        visited[loc][0] += 1 # 방문횟수를 카운트(+1)

        for n_loc in [loc+1, loc-1, loc*2]:
            if 0<=n_loc<MAX and visited[n_loc][0]==0:
                
                # 1) 다음 정점 방문이 처음인 경우 
                if visited[n_loc][1] == -1:
                    visited[n_loc][1] = visited[loc][1] + 1 # 현재시간 +1을 기록하고 큐에 삽입
                    q.append(n_loc)

                # 2) 다음 정점 방문이 처음 아닌 경우 같은 level에서의 방문이어야만 큐에 삽입
                else:
                    if visited[loc][1] + 1 == visited[n_loc][1]:
                        q.append(n_loc)

    print(visited[k][1]) # k에 도달하는 최소탐색시간 출력
    print(visited[k][0]) # k에 도달하는 최소시간 case 개수 출력

if __name__ == "__main__":
    n,k = tuple(map(int,input().split()))
    bfs(n,k)