# https://www.acmicpc.net/problem/11727

def fill_ntiles(n):
    if n<2:
        return 1
    if n<3:
        return 3

    mem = [0 for _ in range(n+1)]
    mem[1] = 1; mem[2] = 3

    for i in range(3,n+1):
        mem[i] = 2*mem[i-2] + mem[i-1]

    return mem[n] % 10007

if __name__ == "__main__":
    n = int(input())
    print(fill_ntiles(n))