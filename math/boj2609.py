# https://www.acmicpc.net/problem/2609

def gcd_recursion(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    mod = n1 % n2
    if mod == 0:
        return n2
    return gcd_recursion(n2, mod)

def lcm(n1, n2, gcd):
    return int((n1*n2)/gcd)

if __name__ == "__main__":
    n1, n2 = tuple(map(int, input().split()))
    gcd = gcd_recursion(n1, n2)
    print(gcd)
    print(lcm(n1, n2, gcd))
