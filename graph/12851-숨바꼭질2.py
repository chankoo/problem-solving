# https://www.acmicpc.net/problem/12851

from collections import deque

def bfs(n,k):
    visited = [0 for _ in range(100001)]
    q = deque([])
    
    q.append(n)
    visited[n] = 1 # n을 방문하고 (현재시간+1)을 마킹

    path_cnt = 0
    min_depth = abs(k-n) # 최소탐색시간 초기화
    while len(q) > 0:
        # q에서 pop 
        loc = q.popleft()

        # loc과 타겟의 위치가 같으면 최단시간에 탐색 성공 -> min_depth 출력
        # if loc==k:
        #     return visited[loc]-1

        for n_loc in [loc+1, loc-1, loc*2]:
            # 보통의 bfs조건에 visited[loc]<min_depth라는 조건 추가
            if (n_loc>=0) and (n_loc<100001) and (visited[n_loc] == 0) and (visited[loc]<min_depth): 
                q.append(n_loc)
                if n_loc == k: # 방금 큐에 넣은 위치가 탐색성공이라면
                    path_cnt += 1 # 경로cnt에 1더하고
                    min_depth = visited[loc] + 1 # min_depth 값 설정가능하다(항상같다)
                    continue
                visited[n_loc] = visited[loc] + 1
    
    print(min_depth-1) # 0에서 시작한 최소탐색시간 출력
    print(path_cnt) # 최소시간탐색 path의 개수 출력


if __name__ == "__main__":
    n,k = tuple(map(int,input().split()))
    bfs(n,k)

