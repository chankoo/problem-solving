# https://www.acmicpc.net/problem/2193

def pinary(n):
    dp  =[1,1,2]

    if n <4:
        return dp[n-1]

    for _ in range(4,n+1):
        dp_last = dp[-1]
        dp[-1] = dp[-3] + 2 * dp[-2]
        dp[-3] = dp[-2]
        dp[-2] = dp_last
    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    print(pinary(n))