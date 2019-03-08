# https://www.acmicpc.net/problem/2941

# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

S = input()
salpha = ['c=','c-','d-','lj','nj','s=','dz=','z=']

count=0
for e in salpha:
    while(e in S):
        S=S.replace(e,' ',1)
        count+=1
S=''.join(S.split())
print(count+len(S))

