# https://www.acmicpc.net/problem/1978
from collections import OrderedDict

N = int(input())
L = list(map(int,input().split()))

# 보다 일반적인 방법(에라토스테네스의 체를 이용한)으로 풀어본다 + ordered dict 사용 연습
# key를 number, value를 해당 num의 소수 여부로 갖는 ordered dict을 만들자
is_prime = OrderedDict().fromkeys(range(1,L[-1]+1),None) 

if 1 in is_prime:
    is_prime[1] = False # 1의 경우는 소수 아님을 명시

while True: # 소수 모두 찾을때까지 반복
    p = None
    for num,val in is_prime.items():
        if val is None: # 판별안된 가장 작은수는 소수
            p = num
            is_prime[num] = True
            break
    
    if p is None: # 모든 수가 판별된 경우 반복 종료
        break

    for num,val in is_prime.items():
        if num <= p: # p까지 판별됨
            continue
        if num % p == 0: # p의 배수는 소수 아님
            is_prime[num] = False

# 주어진 수 중 소수의 개수를 센다
cnt = 0
for l in L:
    cnt += is_prime[l]
print(cnt)