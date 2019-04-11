# https://www.acmicpc.net/problem/2156

# sol
# dp분류를 잘~해야한다. 중복이 있거나 빠트린게 있으면 안된다

import sys

def dp_wine(n):
    global w

    dp = [0 for _ in range(n)]

    dp[0] = w[0]
    if n == 1:
        print(dp[0])
        return 
    
    dp[1] = w[0] + w[1]

    for i in range(2,n):
        # 분류1) ..x, ..o : i번째를 마신다 안마신다
        # 분류2) .ox, .xo, .oo : i-1 번째까지 고려해 가능한 cases
        # 분류3) (oox, xox), (oxo, xxo), (xoo) : i-2 번째까지 고려해 가능한 cases

        case1 = dp[i-1] # (..x)
        case2 = dp[i-2] + w[i] # (.xo)
        case3 = dp[i-3] + w[i-1] + w[i] # xoo

        dp[i] = max(case1, case2, case3)
    
    print(dp[n-1])
    return


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    w = []
    for _ in range(n):
        w.append(sys.stdin.readline())
    w = list(map(int, w))

    dp_wine(n)