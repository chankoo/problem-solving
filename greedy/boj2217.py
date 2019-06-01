# https://www.acmicpc.net/problem/2217

import sys

if __name__ == "__main__":
    N = int(input())
    ropes = []
    for _ in range(N):
        ropes.append(int(sys.stdin.readline().rstrip('\n')))

    ropes = sorted(ropes, reverse=True)

    max_w = ropes[0]
    for i, rope in enumerate(ropes):
        if (i+1) * rope >= max_w:
            max_w = (i+1) * rope
    
    print(max_w)