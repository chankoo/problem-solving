# https://www.acmicpc.net/problem/11053

if __name__ == "__main__":
    n = int(input())
    series = list(map(int, input().split()))

    dp = {}
    for this_idx, this_num in enumerate(series):
        this_val = 1
        for past_num in series[:this_idx]:
            if this_num > past_num:
                this_val = max(this_val, dp[past_num]+1)
        dp[this_num] = this_val
        
    print(max(dp.values()))