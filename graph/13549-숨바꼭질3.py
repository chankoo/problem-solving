# https://www.acmicpc.net/problem/13549

# sol
# loc*2는 q의 앞에서 삽입 해야한다

from collections import deque

def bfs(n,k):
    visited = [0 for _ in range(100001)]
    q = deque([])

    q.append(n)
    visited[n] = 1 # n을 방문하고 (현재시간+1)을 마킹

    while len(q) > 0:
        # q에서 pop 
        loc = q.popleft()

        # loc과 타겟의 위치가 같으면 탐색 성공
        if loc==k:
            return visited[loc] - 1

        n_loc = loc*2
        if (n_loc>=0) and (n_loc<100001) and (visited[n_loc] == 0):
            q.appendleft(n_loc)
            visited[n_loc] = visited[loc]

        for n_loc in [loc+1, loc-1]:
            if (n_loc>=0) and (n_loc<100001) and (visited[n_loc] == 0):
                q.append(n_loc)
                visited[n_loc] = visited[loc] + 1

if __name__ == "__main__":
    n,k = tuple(map(int,input().split()))

    print(bfs(n,k))