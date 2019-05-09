# https://www.acmicpc.net/problem/1182

# TIL
# 파이썬에서 powerset 구현

import itertools

def powerset(iterable):
    set_ = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(set_,r) for r in range(len(set_)+1))

if __name__ == "__main__":
    n, s = tuple(map(int,input().split()))
    arr = list(map(int, input().split()))

    match_cnt = 0
    for el in powerset(arr):
        if sum(el) == s and el != tuple():
            match_cnt += 1
    print(match_cnt)