# https://www.acmicpc.net/problem/9465\

# sol
# 최적값 도출에 두가지 경로가 존재한다. 1) 0번 row에서 시작한 경우 2) 1번 row에서 시작한 경우
# 현재 i번째 컬럼을 진행하면서 두개 경로중 어떤것을 이용할지 미리 알 수 없다
# 그렇기에 dp배열에 두가지 경로의 최적값을 모두 메모하며 진행한다
# i번째 컬럼의 0번 row에 들어갈 최적값은 
#   1) i-1 번째의 1번 row를 포함하는 값
#   2) i-2 번째의 1번 row를 포함하는 값 둘 중 하나이다
# 1)의 경우 정상적인 지그재그 경로를, 2)의 경우 i-1번째를 선택하지 않는 어긋난 경로를 의미한다
# 따라서 dp[0][i] = max[(1), (2)]에 현재값(stic[0][i]) 로 식을 세울 수 있다 

import sys

def get_max_score(stic,n):
    dp = [[0]*(n+1), [0]*(n+1)]

    dp[0][1] = stic[0][1]
    dp[1][1] = stic[1][1]

    for i in range(2,n+1):
        dp[0][i] = max(stic[0][i] + dp[1][i-1], stic[0][i] + dp[1][i-2])
        dp[1][i] = max(stic[1][i] + dp[0][i-1], stic[1][i] + dp[0][i-2])

    return max(dp[0][n], dp[1][n])

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip('\n'))
    for _ in range(t):
        n = int(sys.stdin.readline())
        stic = [[0]+list(map(int, sys.stdin.readline().split()))
                , [0]+list(map(int, sys.stdin.readline().split())) ] 

        print(get_max_score(stic,n))