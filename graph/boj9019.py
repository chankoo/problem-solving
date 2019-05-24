# https://www.acmicpc.net/problem/9019

# sol
# 위치를 기준으로 bfs 함수를 정의한다 
# D, S, L, R 각 연산을 정의하고 bfs 함수 내에서 각 연산의 결과를 큐에 넣는다
# 방문체크 시 현재 위치 도달에 [사용한 연산, 이전 위치] 두가지 정보를 저장하여 path의 역추적을 가능케한다
## 주의할점 
## 1) 큐에 연산이 아니라 위치가 들어가야함
## 2) 각 위치에서 가지가 갈라져야(bfs)하므로 계산기 객체를 구현하여 자원과 연산을 관리하는 것은 비효율적
## 3) 시간초과(L, R 연산)

# TIL
# %와 //을 이용하여 십진수의 shift 연산 구현

import sys
from collections import deque

def D(n):
    return 2*n % 10000

def S(n):
    if n == 0:
        return 9999
    return n - 1

def L(n):
    return (n%1000)*10+(n//1000)

def R(n):
    return (n//10)+(n%10)*1000

def calc(n, op):
    if op == 'D':
        return D(n)
    elif op == 'S':
        return S(n)
    elif op == 'L':
        return L(n)
    elif op == 'R':
        return R(n)

def is_equal(next_, target):
    if next_ == target:
        return True
    return False

def back_track(now, path):
    prev = visited[now][1]
    if prev == -1:
        print(path[:-1])
        return
    path = visited[now][0] + path
    back_track(prev, path)

def bfs(init, target):
    q = deque([init])
    visited[init] = ['', -1]

    while len(q) > 0:
        now = q.popleft()
        for op in ['D', 'S', 'L', 'R']:
            next_ = calc(now, op)
            if visited[next_] == -1:
                q.append(next_)
                visited[next_] = [op, now] # [next_ 방문에 이용한 연산, 이전 위치]를 저장
                if is_equal(next_, target):
                    back_track(next_, op)
                    return

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip('\n'))

    for _ in range(T):
        input_ = sys.stdin.readline().rstrip('\n').split()

        visited = [-1 for _ in range(10000)]
        bfs( int(input_[0]), int(input_[1]) )