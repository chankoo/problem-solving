# https://www.acmicpc.net/problem/1011

T = int(input())

for i in range(T):
    tmp = input().split()
    dst = int(tmp[1])-int(tmp[0])
    kSum=0;cnt1=0;cnt2=0
    while True:
        cnt1+=1
        kSum+=cnt1
        if kSum>=dst:
            break
        cnt2+=1
        kSum+=cnt2
        if kSum>=dst:
            break
    
    print(cnt1+cnt2)
    