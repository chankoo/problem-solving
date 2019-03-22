# https://www.acmicpc.net/problem/9095

# sol
# dp를 위해서는 문제를 분할하여 부분문제를 만드는 것이 핵심
# 단, 부분문제는 MECE(Mutually Exclusive Collectively Exhaustive) 해야한다
# 이 문제의 경우 recur_case(10) = recur_case(9) + recur_case(8) + recur_case(7) 라 표현가능하다
# 왜냐면 1,2,3 에서 시작하는 각각의 MECE한 case(부분문제)가 있고, 이를 합계 10으로 만드는 경우의 수가 각각 recur_case(9), recur_case(8), recur_case(7)이기 때문

def recur_case(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4

    return recur_case(n-1) + recur_case(n-2) + recur_case(n-3)

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        print(recur_case(int(input())))
