# https://www.acmicpc.net/problem/2960

N,K = map(int, input().split())

ints = list(range(2,N+1)) # 1) 2부터 N까지 모든 정수를 적는다.
primes = []

rm_lst = []
while (len(ints) > 0 and len(rm_lst)< K):
    p = ints.pop(0) # 2) 아직 지우지 않은 수 중 가장 작은 수(p)를 찾는다. 이는 소수이고, 지운다
    rm_lst.append(p)
    primes.append(p)
    
    p_muls = [] # 3) p 의 배수를 찾는다
    for i in ints: 
        if i%p == 0:
            p_muls.append(i)
        else:
            pass

    for p_mul in p_muls:
        rm_lst.append(p_mul)
        ints.remove(p_mul) # 4) p의 배수를 크기 순서대로 지운다
    
    # 5) 아직 모든 수를 지우지 않았다면, 다시 2)로 간다.

print(rm_lst[K-1])



