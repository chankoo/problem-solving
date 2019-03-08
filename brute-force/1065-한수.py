# https://www.acmicpc.net/problem/1065

N = int(input())
def isHansoo(n):
    s=str(n)
    if len(s)==1 or len(s)== 2:
        return 1
    count = 1
    diff = int(s[1])-int(s[0])
    for i in range(1,len(s)-1):
        if ( int(s[i+1])-int(s[i]) )==diff:
            count+=1
    if count==len(s)-1:
        return 1
    else: return 0
Sum=0
for n in range(1,N+1):
    if isHansoo(n)==1:
        Sum+=1
print(Sum)