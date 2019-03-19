# https://www.acmicpc.net/problem/1463

# sol
# dp 문제로 지정되었지만 bfs로 간단하게 해결가능

from collections import deque

def bfs(x):
    visited = [-1 for _ in range(x+1)]
    q = deque([])

    q.append(x)
    visited[x] = 0

    while len(q) > 0:
        now = q.popleft()
        if now == 1:
            return visited[1]

        if 1 < now:
            if (now % 3 == 0) and (visited[now//3] == -1):
                next_ = now // 3
                visited[next_] = visited[now] + 1
                q.append(next_)

            if (now % 2 == 0) and (visited[now//2] == -1):
                next_ = now // 2
                visited[next_] = visited[now] + 1
                q.append(next_)

            if (visited[now-1] == -1):
                next_ = now - 1 
                visited[next_] = visited[now] + 1
                q.append(next_)

if __name__ == "__main__":
    x = int(input())

    print(bfs(x))