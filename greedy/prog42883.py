# https://programmers.co.kr/learn/courses/30/lessons/42883

# sol
# greedy하게 푸는 가장 큰수 만들기 문제
# 현재 자리수에 위치 가능한 배열중 max값을 현재 자리수로 선택한다

def solution(number, k):
    num_len = len(number)
    
    answer = ''
    start = 0
    rep = num_len - k
    while rep > 1:
        window = number[start: (-rep+1)]
        local_max = '-1'
        local_max_idx = None
        for i, num in enumerate(window):
            if num > local_max:
                local_max = num
                local_max_idx = start + i
        
        rep -= 1
        start = local_max_idx+1
        answer += local_max
    
    answer += max(number[start:])
    return answer

