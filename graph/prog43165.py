# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    len_num = len(numbers)
    answer = 0
    
    def dfs(idx, signs):
        nonlocal answer, numbers, target, len_num
        if idx+1 == len_num:
            output = sum([signs[i]*numbers[i] for i in range(len_num)])
            if output == target:
                answer += 1
            return

        for sign in [1, -1]:
            dfs(idx+1, signs[:]+[sign])

    signs = []
    dfs(0, signs[:]+[1])
    dfs(0, signs[:]+[-1])
    return answer

if __name__ == "__main__":
    solution([1, 1, 1, 1, 1], 3)