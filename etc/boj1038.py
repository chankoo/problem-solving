# https://www.acmicpc.net/problem/1038

# sol
# dp와 브루트포스로 풀었으나 시간초과였다.
# 그래서 대신 큐를 이용하는 간단한 풀이를 적용하였다
# 감소하는 수의 특성상, 현재 큐에서 뽑힌 수 num의 마지막자리 숫자보다 작은 수를 num의 끝에 붙여 큐에 삽입한다
# 예를 들면 432가 뽑혔을때 4321과  4320이 큐에 삽입된다
# 그 결과 오름차순으로 정렬된 모든 감소하는 수가 큐를 거쳐가게된다

from collections import deque

def decreasing_q(n):
    if n < 10:
        print(n)
        return 
    q = deque()
    for i in range(1,10):
        q.append(i)
    
    order = 0
    while len(q) > 0:
        num = q.popleft()
        order += 1

        if n==order:
            print(num)
            return
        str_num = str(num)
        for last in range(10):
            if last >= int(str_num[-1]):
                break
            q.append(int(str_num + str(last)))

    print(-1)
    return

if __name__ == "__main__":
    n = int(input())
    decreasing_q(n)


