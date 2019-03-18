# https://www.acmicpc.net/problem/13913

# sol
# path를 역추적 가능하게 현재 위치의 인덱스에 이전의 위치를 저장하는 배열 links를 구현한다

from collections import deque

def bfs(n,k):
    visited = [0 for _ in range(100001)]
    links = [-1 for _ in range(100001)] # 위치간 링크 정보를 저장하는 배열
    q = deque([])
    
    q.append(n)
    visited[n] = 1 # n을 방문하고 (현재시간+1)을 마킹

    while len(q) > 0:
        # q에서 pop 
        loc = q.popleft()

        # loc과 타겟의 위치가 같으면 탐색 성공 -> path 출력하자
        if loc==k:
            print(visited[loc]-1)
            break

        for n_loc in [loc+1, loc-1, loc*2]:
            if (n_loc>=0) and (n_loc<100001) and (visited[n_loc] == 0):
                q.append(n_loc)
                visited[n_loc] = visited[loc] + 1
                links[n_loc] = loc # path 추적위해서 n_loc이 어느 loc에서 왔는지 저장
    
    path = deque([])
    path.appendleft(loc) # 탐색종료점(추적시작점) 위치 삽입
    while links[loc] != -1: # 존재하는 링크의 끝까지
        path.appendleft(links[loc]) # 역추적하며 위치 삽입
        loc = links[loc]
    
    for loc in path:
        print(loc,end=' ')

if __name__ == "__main__":
    n,k = tuple(map(int,input().split()))

    bfs(n,k)