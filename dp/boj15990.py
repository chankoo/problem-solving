# https://www.acmicpc.net/problem/15990

# sol
# boj15989 1,2,3 더하기 4와 유사한 풀이다
# 정수 i를 만드는 경우의 수를 각각 1,2,3으로 시작한 case로 분류하고 
# 2차원 배열 mem에 쌓아나간다
# 이때, mem[i][0] = mem[i-1][1] + mem[i-1][2] 로 표현가능하다
# i를 1로 시작해서 만드는 case구하는 것이고, 이는 i-1을 2로 시작해 만든 case와 3으로 시작해 만든 case의 합이기 때문이다
# 메모리 문제 때문에 cache 배열을 구현

from collections import deque
import sys
def case_cnt(n):
    mem = deque([])
    # 기저 case 설정
    mem.append([1,0,0]) # n==1 case (1)
    mem.append([0,1,0]) # n==2 case (2)
    mem.append([1,1,1]) # n==3 case (1+2, 2+1, 3)

    if n < 4: # 4미만일 경우 기저 case를 리턴
        return sum(mem[n-1])

    cache = mem # mem을 모두 저장하지말고 cache로 관리
    for _ in range(3,n): # from 4 to N까지
        this_val = deque([])
        this_val.append(cache[-1][1] + cache[-1][2]) # 1로 시작해 정수 row를 만드는 경우의 수
        this_val.append(cache[-2][0] + cache[-2][2]) # 2로 시작해 정수 row를 만드는 경우의 수
        this_val.append(cache[-3][0] + cache[-3][1]) # 3로 시작해 정수 row를 만드는 경우의 수

        cache.append(this_val) # cache의 마지막 요소로 추가
        cache.popleft() # 기억할 필요없어진 cache의 첫번째 요소 삭제
    return sum(cache[-1]) % 1000000009

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    tc = tuple(map(int, [sys.stdin.readline() for _ in range(t)]))
    for case in tc:
        print(case_cnt(case))
        