# https://www.acmicpc.net/problem/10844

# TIL
# cache가 아니라 전체 배열을 저장하는 코드로는 런타임 에러가 난다
# 왜 메모리 초과가 아닌 런타임 에러인지는 확실히 모르겠으나 조심하자

import sys
from collections import deque

def stair_num(n):
    mod = 1000000000
    dp = deque([]) # dp[3][j]: n,n-1,n-2 번째를 수 일때를 저장, j <= 해당 자리수로 만들 수 있는 case 개수 
    dp.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1]) # n==1 일때 초기값
    dp.append([0, 2, 2, 2, 2, 2, 2, 2, 2, 1]) # n==2
    if n==1:
        return sum(dp[0])

    for _ in range(3,n+1): # 3 to n
        new_row = [0 for _ in range(10)] # 순회중인 수의 cnt를 초기화
        for j in range(10): # 0 to 9
            if j == 0:
                new_row[j] = 0
            
            elif j == 9:
                new_row[j] = (dp[-1][j-1]) # 98*~ 의 경우이다
            
            elif j == 1:
                new_row[j] = (dp[-1][j+1] + dp[-2][j]) % mod # 12*~ 이나 101*~의 경우

            else:
                new_row[j] = (dp[-1][j-1] + dp[-1][j+1]) % mod #j(j-1)*~이나 j(j+1)*~의 경우
        
        dp.append(new_row) # 완성한 i번째를 dp에 추가
        dp.popleft() # 필요없어진 old memory 삭제
    return sum(dp[-1]) % mod
    

if __name__ == "__main__":
    n = sys.stdin.readline()
    print(stair_num(int(n)))