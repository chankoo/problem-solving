# https://www.acmicpc.net/problem/1463

# sol
# 1 부터 메모이제이션하며 배열을 채워간다
# 즉, 1부터 해당 정수를 최소한의 연산으로 만드는 방법을 계산하여 역으로 답을낸다
# arr[n] = min(arr[n/2],arr[n/3],arr[n-1]) + 1
# O(n) 시간에 답을 낼 수 있다
## 현재 배열의 원소를 모두 계산하고 있기에 bfs로 구현한 결과보다 살짝 느리다


def to_one(n):
    arr = [0 for _ in range(n+1)] # 1 ~ n 의 인덱스를 이용한다

    for i, cnt in enumerate(arr):
        if i==0 or i==1:continue
        
        cnt_candi = []
        if i%3 == 0:
            cnt_candi.append(arr[i//3] + 1)
        if i%2 == 0:
            cnt_candi.append(arr[i//2] + 1)
        if i>1:
            cnt_candi.append(arr[i-1] + 1)

        if len(cnt_candi) == 0:
            continue
        
        arr[i] = min(cnt_candi)
    
    return arr[n]


if __name__ == "__main__":
    n = int(input())
    print(to_one(n))