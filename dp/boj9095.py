# https://www.acmicpc.net/problem/9095

# sol
# dp를 나름대로 설명해보자면
# 1) 문제를 분할하여 부분문제를 만들고
# 2) 부분문제의 최적해를 메모해서 다른 부분문제를 풀때 부분 최적해를 자꾸 가져다 쓰는 방법
# 부분문제는 MECE(Mutually Exclusive Collectively Exhaustive)하게 분할해야한다
# 이 문제의 경우 recur_case(10) = recur_case(9) + recur_case(8) + recur_case(7) 라 표현가능하다
# 왜냐면 1,2,3 에서 시작하는 각각의 MECE한 case(부분문제)가 있고, 이를 합계 10으로 만드는 경우의 수가 각각 recur_case(9), recur_case(8), recur_case(7)이기 때문

def recur_case(n):
    global mem

    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4

    if mem[n] != -1:
        return mem[n]
    
    mem[n] = recur_case(n-1) + recur_case(n-2) + recur_case(n-3)
    
    return mem[n]

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        mem = [-1 for _ in range(n+1)]
        print(recur_case(n))
