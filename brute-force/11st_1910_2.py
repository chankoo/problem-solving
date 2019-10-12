"""
문제 설명
n명의 사람이 일렬로 서있습니다. 이때, 사람들이 서 있는 순서를 바꾸려고 합니다. 맨 앞부터 1번째, 2번째, ... n번째 사람의 키가 주어지면, |1번째 사람의 키 - 2번째 사람의 키| + |2번째 사람의 키 - 3번째 사람의 키| + ... + |n-1번째 사람의 키 - n번째 사람의 키| 의 값이 최대가 되도록 바꾸면 됩니다. (|k|는 절댓값을 나타냅니다)
사람들의 키가 들어있는 배열 v가 매개변수로 주어질 때, 위의 식을 만족하는 최댓값을 return 하도록 solution 함수를 완성해 주세요.

제한사항
v의 길이 (사람 수 n)는 2 이상 8 이하의 자연수입니다.
v의 원소(사람들의 키)는 1 이상 100 이하의 자연수입니다.
입출력 예
v	answer
[20,8,10,1,4,15]	62
사람들을 [10,4,20,1,15,8] 로 배치하면, |10-4|+|4-20|+|20-1|+|1-15|+|15-8|=6+16+19+14+7=62가 됩니다. 이 경우가 문제에 주어진 식의 최댓값이므로 62를 return 합니다.

풀이
배열 v의 최대 길이가 8이므로 가능한 경우의수는 8! = 40320 으로 크지않다. 가능한 모든 배열의 경우를 완전탐색하여 최댓값을 구한다.
함수 dfs_to_make_idx_arr로 가능한 모든 경우에 대해 새로운 배열 idx_arr를 만든다. 값이 아니라 인덱스의 배열을 만드는 것은 사람들의 키가 모두 다르다는 조건이 없기 때문이다.
인덱스 배열의 길이가 원래 주어진 배열 길이와 같아지면 함수 get_a_score_from_idx_arr로 score를 계산, max_score와 비교해 갱신한다.
"""

from copy import deepcopy
from collections import deque

def get_a_score_from_idx_arr(heights, idx_arr):
    score = 0
    for i, idx in enumerate(idx_arr):
        if i == 0:
            continue
        score += abs(heights[idx_arr[i-1]] - heights[idx])
    return score


def dfs_to_make_idx_arr(len_v, idx_arr, heights):
    global max_score

    if len(idx_arr) == len_v:
        idx_arr = list(idx_arr)
        this_score = get_a_score_from_idx_arr(heights, idx_arr)
        if max_score < this_score:
            max_score = this_score
        return
    
    copied_idx_arr = deepcopy(idx_arr)
    for idx in range(len_v):
        if idx not in copied_idx_arr:
            copied_idx_arr.append(idx)
            dfs_to_make_idx_arr(len_v, copied_idx_arr, heights)
            copied_idx_arr.pop()


def solution(v):
    global max_score
    max_score = 0
    idx_arr = deque()
    len_v = len(v)
    
    dfs_to_make_idx_arr(len_v, idx_arr, v)
    print(max_score)


if __name__ == "__main__":
    heights = [20,8,10,1,4,15,92,98]
    solution(heights)