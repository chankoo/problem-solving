"""
문제 설명
철수의 생일을 맞아 XX 식당에서 생일 파티를 하기로 했습니다. 생일 파티를 하는 XX 식당까지는 택시를 타고 이동하기로 했습니다. 철수의 친구들은 친한 친구들끼리 그룹을 구성하고 있으며, 한 사람당 하나의 그룹에만 속해 있습니다. 택시를 탈 때는 반드시 같은 그룹에 속한 친구들은 같은 택시를 타기로 했으며, 한 택시에는 여러 그룹이 함께 탈 수 있습니다. 단, 택시에는 최대 4명까지 함께 탑승 가능합니다. 각 그룹의 구성원 수가 들어있는 배열 s가 매개변수로 주어질 때, 필요한 택시의 수의 최솟값을 return 하도록 solution 함수를 완성해주세요.

주의사항
s는 각 그룹별 구성원 수가 들어있는 배열이며, 배열의 길이(그룹의 수)는 100,000 이하의 자연수입니다.
각 그룹의 구성원 수는 4 이하의 자연수입니다.

입출력 예
s | output

[1,2,4,3,3] | 4
[2,3,4,4,2,1,3,1] | 5

입출력 설명
입출력 예 #1 
한 그룹당 하나씩의 택시를 이용한다면 총 5대의 택시가 필요합니다. 그러나 다음과 같이 탑승한다면 4대의 택시만으로도 충분합니다.
첫 번째 그룹(1명)과 네 번째 그룹(3명)이 같은 택시를 탑니다.
그 외 나머지 그룹은 모두 다른 택시를 탑니다.

입출력 예 #2 
한 그룹당 하나씩의 택시를 이용한다면 총 8대의 택시가 필요하지만, 다음과 같이 탑승한다면 5대의 택시만으로도 충분합니다.
첫 번째 그룹(2명)과 다섯 번째 그룹(2명)이 같은 택시를 탑니다.
두 번째 그룹(3명)과 여섯 번째 그룹(1명)이 같은 택시를 탑니다.
일곱 번째 그룹(3명)과 여덟 번째 그룹(1명)이 같은 택시를 탑니다.
그 외 나머지 그룹은 모두 다른 택시를 탑니다.

"""

# sol
# 케이스를 나눠 그리디하게 푼다. 코드는 그닥 깔끔하지 못하다

def solution(s):
    taxi_cnt = 0
    resid = {}

    # 4인 경우 바로 택시에 타고 resid 딕셔너리에 나머지를 저장한다
    for num in s:
        if num == 4:
            taxi_cnt += 1
        else:
            if num in resid:
                resid[num] += 1
            else:
                resid[num] = 1
    
    # 3인 그룹은 1과 함께 4를 만드는 것이 최선이므로 3과 1로 택시에 탄다
    temp_cnt = min(resid[3], resid[1])
    taxi_cnt += temp_cnt
    resid[3] -= temp_cnt
    resid[1] -= temp_cnt

    if resid[3] > 0:
        taxi_cnt += resid[3]
        resid[3] = 0
    else:
        pass

    # 남은 2와 1로 경우를 나누어 해결한다
    temp_cnt = resid[2]//2
    taxi_cnt += temp_cnt

    if resid[2] % 2 == 0:
        resid[2] = 0
        
        taxi_cnt += resid[1] // 4
        if resid[1] % 4 == 0:
            pass
        else:
            taxi_cnt += 1

    else:
        resid[2] = 1

        if resid[1] >= 2:
            taxi_cnt += 1
            resid[1] -= 2
            resid[2] = 0
            taxi_cnt += resid[1] // 4
            if resid[1] % 4 == 0:
                pass
            else:
                taxi_cnt += 1
        
        else:
            taxi_cnt += 1
    
    return taxi_cnt

if __name__ == "__main__":
    solution(list(map(int,input().split())))