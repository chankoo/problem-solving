# 19.09.28

stic1 = [12,12,12,12,12]
stic2 = [12,80,14,22,100]

def get_maximum(stic):
    stic_len = len(stic)
    dp = [0]*stic_len  # stic_len 만큼 dp배열 생성
    
    # 초기화
    dp[0] = stic[0]
    dp[1] = max((stic[0], stic[1]))

    # dp
    for i in range(2, stic_len):
        dp[i] = max((stic[i]+dp[i-2], dp[i-1] ))
    
    return dp[-1]


if __name__=="__main__":
    get_maximum(stic1)
    get_maximum(stic2)