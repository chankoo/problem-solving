# https://www.acmicpc.net/problem/9613

import sys
import itertools

input = sys.stdin.readline

def gcd_recursion(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    mod = n1 % n2
    if mod == 0:
        return n2
    return gcd_recursion(n2, mod)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        case = list(map(int, input().split()))[1:]
        
        sum_of_gcds = 0
        for n1,n2 in itertools.combinations(case, 2):
            sum_of_gcds += gcd_recursion(n1,n2)
            
        print(sum_of_gcds)
