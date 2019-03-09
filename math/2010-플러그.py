# https://www.acmicpc.net/problem/2010

N = int(input())
plugs =1
for i in range(N):
    tmp = int(input())
    plugs = plugs+ tmp -1
print(plugs)