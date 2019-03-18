# https://www.acmicpc.net/problem/17071

from collections import deque

# 현재 depth(흐른 시간)의 타겟 위치 구하는 함수
def calc_target_loc(k, depth): 
    return k+sum(range(depth))

def bfs(n,k):
    visited = [0 for _ in range(500001)]
    target = [0 for _ in range(500001)]
    q = deque([])

    q.append(n)
    visited[n] = 1 # n을 방문하고 (현재시간+1)을 마킹
    target[k] = 1 # 타겟의 위치 k에 (현재시간+1)을 마킹

    while len(q) > 0:
        # q에서 pop 
        loc = q.popleft()
        # print('loc: {}'.format(loc))

        if calc_target_loc(k,visited[loc]) > 500000: # 찾는 위치가 500,000을 넘을 경우
            return -1
        
        # 현재 시간에 loc과 타겟의 위치가 같으면 탐색 성공
        if (loc == calc_target_loc(k,visited[loc])):
            # print(visited[:100])
            return visited[loc] - 1

        for n_loc in [loc+1, loc-1, loc*2]:
            if (n_loc>=0) and (n_loc<500001) and (visited[n_loc] == 0):
                q.append(n_loc)
                visited[n_loc] = visited[loc] + 1
    print(visited[:100])

if __name__ == "__main__":
    n,k = tuple(map(int,input().split()))

    print(bfs(n,k))