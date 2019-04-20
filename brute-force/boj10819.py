# https://www.acmicpc.net/problem/10819

import sys
import itertools

def get_diff(arr):
    diff_sum = 0
    for i in range(len(arr)-1):
        diff_sum += abs(arr[i]-arr[i+1])
    return diff_sum

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip('\n'))
    arr = list(map(int, sys.stdin.readline().split()))

    max_diff = 0
    for this in list(itertools.permutations(arr,len(arr))):
        max_diff = max(max_diff, get_diff(this))

    print(max_diff)