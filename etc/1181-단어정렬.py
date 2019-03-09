# https://www.acmicpc.net/problem/1181

N = int(input())
L = [input()]
for i in range(N-1):
    j=0
    l = input()
    if l in L:
        continue
    while j<len(L):
        if len(L[j])>len(l):
            L.insert(j,l)
            break
        elif len(L[j])==len(l):
            for k in range(len(l)):
                if ord(L[j][k]) < ord(l[k]):
                    if j==len(L)-1:
                        L.append(l)
                    break
                elif ord(L[j][k]) > ord(l[k]) :
                    L.insert(j,l)
                    j = len(L)
                    break
                else:
                    continue
        else:
            if j==len(L)-1:
                L.append(l)
        j+=1
for l in L:
    print(l)