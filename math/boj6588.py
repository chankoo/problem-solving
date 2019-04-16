# TIL
# 효율이 좋은 소수 판별 알고리즘

import sys

limit = 1000000
is_prime = [False for _ in range(limit+1)]

for i in range(2, limit+1):
    if i*i > limit:
        break
    if is_prime[i] is False:
        for j in range(i*i, limit+1, i):
            is_prime[j] = True


if __name__ == "__main__":
    while True:
        n = int(sys.stdin.readline())
        if n is 0:
            break
        for i in range(2, limit+1):
            if is_prime[i] is False:
                j = n - i
                if is_prime[j] is False:
                    print(n, "=", i, "+", j)
                    break