# https://www.acmicpc.net/problem/4673

def d(n):
    sum_ = n
    num_to_str = str(n)

    for s in num_to_str:
        sum_ += int(s)
    return sum_

nums = [n for n in range(1,10001)]
is_self = [False for _ in range(1,10001)]

for i in range(1,10001):
    n = i
    while True:
        n = d(n)
        if ( (n>=10000) or (is_self[n]==True) ):
            break
        is_self[n] = True

for i in range(1,10000):
    if is_self[i] == False:
        print(i)

