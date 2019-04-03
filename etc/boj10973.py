# https://www.acmicpc.net/problem/10973

import sys
import copy

def prev_permut(N):
    i_found = -1
    for i,_ in enumerate(N[:-1]):
        if N[i] > N[i+1]:
            i_found = i

    if i_found == -1: # 첫번째 순열의 경우 return -1
        return -1
    
    j = -1 
    while True: # N을 역순회하는 인덱스 j에 대해
        if N[j] < N[i_found]: # 무조건 존재하는 N[j] > N[기준이되는i] 를 찾으면 swap
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

    print(prev_permut(N))