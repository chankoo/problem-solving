# https://www.acmicpc.net/problem/10972

# TIL
# 다음 순열 찾기 알고리즘
# 특정 순열의 바로 다음 순열을 찾는 O(N) 알고리즘이다
# 직관적으로 떠오르지 않았기에 기억해두자
# 1) 순열(N)을 순회하며 N[i] < N[i+1] 인 i의 max를 찾는다. 없다면 return -1이다
# 2) N의 끝 인덱스에서 i+1 까지 역으로 순회하며(j: N[-1] to N[i+1]) N[j] > N[i] 인 첫번째 j를 찾는다
# 3) swap(N[i], N[j])
# 4) N[i+1] ~ N[-1] 을 reverse 해준다
# https://jins-dev.tistory.com/entry/%EB%8B%A4%EC%9D%8C-%EC%88%9C%EC%97%B4-%EC%B0%BE%EA%B8%B0-%EC%A0%84%EC%B2%B4-%EC%88%9C%EC%97%B4-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Next-Permutation

import sys
import copy

def next_permum(N):
    i_found = -1
    for i,_ in enumerate(N[:-1]):
        if N[i] < N[i+1]:
            i_found = i

    if i_found == -1: # 마지막 순열의 경우 return -1
        return -1
    
    j = -1 
    while True: # N을 역순회하는 인덱스 j에 대해
        if N[j] > N[i_found]: # 무조건 존재하는 N[j] > N[기준이되는i] 를 찾으면 swap
            temp = N[j]
            N[j] = N[i_found]
            N[i_found] = temp
            break
        j += -1
    
    reversed_N = N[:i_found+1] + copy.deepcopy(N[i_found+1:])[::-1] # N[i+1:]를 역순으로 뒤집어 리턴
    return ' '.join(map(str,reversed_N))


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    N = list(map(int, sys.stdin.readline().split()))

    print(next_permum(N))
    