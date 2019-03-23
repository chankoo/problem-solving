# https://www.acmicpc.net/problem/15988

# sol
# prices[0 ~ n-1] 배열이 주어진다. price[i]에 (i+1)개로 구성된 카드팩의 가격을 갖는 배열이다
# costs[0 ~ n-1] 배열을 초기화한다. costs[i]에 (i+1)개 카드 갖기위한 최소금액을 저장한다
# 0 ~ n-1의 순회동안 현재 위치 i에서의 문제를 부분문제로 나누고 금액을 비교하여 최소금액을 저장한다
# 즉, 3개 카드를 얻는 최소금액을 구하는 문제는 2개 카드를 얻는 최소금액(costs[1])에 1개짜리 카드팩의 금액(prices[0])을 더한 것이거나 1개 카드 얻는 최소금액(costs[0])에 2개짜리 카드팩의 금액(prices[1]) 을 더한 것이거나 3개짜리 카드팩의 금액(prices[2]) 일 수 있다
# 이 3가지 경우의 최소값이 3개 카드 얻는 최소금액이다
# 수식으로 쓰면 costs[i] = minimum[(costs[i-1]+prices[0]), (costs[i-2]+prices[1]), ...  ) 
# costs 배열을 완성한 후 n-1번째(n개 카드 얻는 최소금액)을 출력한다

def get_min_cost(n, prices):
    if len(prices) == 1:
        return prices[0]
    
    costs = [0 for _ in range(n)]
    costs[0] = prices[0] # 1개 카드 얻는 최소금액은 1개짜리 카드팩 가격으로 고정
    for i in range(1,len(costs)):# 2개~n개 카드 얻는 최소금액 배열을 완성하자 
        this_cost = prices[i] # (i+1)개 카드얻는 최소금액의 초기화 -> (i+1)개짜리 카드팩의 가격
        for j in range(1,i+1): # 최소금액과 부분문제의 최소금액들을 비교해 최소금액을 갱신
            tmp_cost = costs[i-j]+prices[j-1]
            if tmp_cost<this_cost:
                this_cost = tmp_cost
        
        costs[i] = this_cost # (i+1)개 카드얻는 최소금액을 확정

    return costs[n-1]

if __name__ == "__main__":
    n = int(input())
    prices = tuple(map(int,input().split()))
    print(get_min_cost(n,prices))