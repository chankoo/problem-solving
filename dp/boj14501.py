# https://www.acmicpc.net/problem/14501

# sol
# n <= 15 라 완전탐색도 가능하지만 dp로 풀어보자
# dp[1~n]에 최적값을 기록한다. dp[i]는 i번째 날부터 퇴근날까지의 max pay이다
# T[i]는 i번째 날의 작업을 마치는데 걸리는 시간이고 P[i]는 그 작업의 pay다
# i번째날의 작업을 1) 수행하지 않는다, 2) 수행한다의 2가지 case가 있고 둘중 max값을 dp[i]에 저장한다
# 1) 수행하지 않을 경우 dp[i]는 전날과 같으므로 dp[i+1]이고 
# 2) 수행할 경우 dp[i]는 해당 작업에 소요되는 날짜만큼 거슬러 올라간 날짜(i+T[i])의 최적값(dp[i+T[i]])에 현재 작업의 pay(P[i])를 더한 값이 된다   
# 점화식을 세우면, dp[i] = max(dp[i+1], dp[i+T[i]] + P[i])
## dp[i]를 위해 dp[i+1] 과 dp[i+T[i]] 가 미리 계산되어야하므로 dp 배열의 뒤쪽부터 채워나간다
## 인덱스 조심

#TIL
# dp의 의미: 부분문제의 최적값을 메모이제이션하며 중복되는 계산없이 한번에 전체문제를 푸는 것
# dp의 조건
# 1) 부분문제로 나눌수있다
# 2) 부분문제의 최적값을 모으면 전체문제의 최적값이다

import sys

def fill_dp(n):
    global dp, T, P

    dp[n+1] = 0 # 인덱스 조정을 위한 배열
    dp[n] = 0
    if T[n] == 1:
        dp[n] = P[n]
    
    for i in range(n-1,0,-1):
        if i+T[i] < n+2:
            dp[i] = max(dp[i+1], dp[i+T[i]]+P[i])
        else:
            dp[i] = dp[i+1]
    
    print(dp[1])
    return

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = [0 for _ in range(n+2)]
    T = [0,]
    P = [0,]
    
    for _ in range(n):
        t, p = tuple(map(int, sys.stdin.readline().split()))
        T.append(t)
        P.append(p)

    fill_dp(n)
