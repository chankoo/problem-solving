# https://www.acmicpc.net/problem/15989

# sol
# boj9095와 다른 점은 합을 이루는 수의 순서까지 고려해야한다는 점이다
# 즉, (1+3)과 (3+1)은 순서만 다를 뿐 같은 경우로 쳐야하기에 순서를 생각하여 풀어야한다
# 간단한 방법은 임의로 순서를 부여하는 것이다. 그러니까 문제를 풀때 1,2,3이 합해지는 순서가 비오름차순으로 진행된다는 제약을 부여한다
# 구현을 위해 메모이제이션을 위한 2차원 배열 mem을 생각한다. axis=0으로 정수 n을 쌓아가며 1,2,3 으로 시작해서 해당 정수를 만드는 합의 개수를 저장한다
#   1 2 3
# 1 1 0 0
# 2 1 1 0
# 3 1 1 1
# 4 1 2 1 
# 5 1 2 2
# 6 1 3 3
# ...
# 일반화하면 mem[n][i] = sum(mem[n-(i+1)][0] + mem[n-(i+1)][1] ... + mem[n-(i+1)][i])

from collections import deque

def case_cnt(n):
    mem = deque([])
    
    mem.append([1,0,0]) # n==1
    mem.append([1,1,0]) # n==2
    mem.append([1,1,1]) # n==3

    if n < 4:
        return sum(mem[n-1])

    for row in range(3,n): # n from 4 to N까지
        this_val = []
        this_val.append(mem[row-1][0]) # 1 이하의 수로 정수 row를 만드는 경우의 수
        this_val.append(mem[row-2][0] + mem[row-2][1]) # 2 이하의 수로 정수 row를 만드는 경우의 수
        this_val.append(mem[row-3][0] + mem[row-3][1] + mem[row-3][2]) # 3 이하의 수로 정수 row를 만드는 경우의 수
        mem.append(this_val)
    return sum(mem[n-1])

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(case_cnt(int(input())))




