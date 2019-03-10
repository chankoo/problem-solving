# https://www.acmicpc.net/problem/14500

# solution
# 1) 초기 좌표 (i,j)를 정한다   
# 2) 인접한 좌표에 대해 dfs 하며 4개 블럭으로 가능한 합의 최대값을 갱신한다
# 3) dfs 불가능한 'ㅗ' 모양 블럭으로 가능한 값을 계산해 최대값을 갱신한다
# 4) 1)로 돌아가 새로운 초기 좌표(i, j) 정한다. brute-forcely 순회한다
# 5) 순회를 마치고 최대값을 출력한다

# TIL
# O(N)인 초기화 함수(reset_visited)를 brute-force에 이용하는 것은 가볍지 않은 코드이다. 결과적으로 O(N^2)가 된다


# 테트로미노의 길이인 4 level 동안 현재 노드에서 가능한 방향을 모두 탐색하는 dfs 함수
def dfs(i,j,cnt,this_sum):
    global nums, visited, max_sum
    di = [1,0,-1,0] # row 방향 움직임
    dj = [0,1,0,-1] # col 방향 움직임

    if cnt == 4: # 4번째 블럭까지 계산했을때 
        max_sum = max(this_sum, max_sum) # global max_sum보다 크면 갱신
        return

    for d_idx in range(4):
        next_i = i+di[d_idx]
        next_j = j+dj[d_idx]

        if ( (next_i < N) and (next_i >= 0) and (next_j < M) and (next_j >= 0) and visited[next_i][next_j] == False ):
            visited[next_i][next_j] = True
            dfs(next_i, next_j, cnt+1, this_sum+nums[next_i][next_j])
            visited[next_i][next_j] = False

# 'ㅗ' 모양 블럭의 경우 dfs 탐색이 불가(revisit 필요)하기에 따로 계산 해주자
def sum_directly(locations:list): # 4블럭의 좌표롤 모두 받아 값을 계산하는 함수
    global nums
    sum_d = 0
    for loc in locations:
        sum_d += nums[loc[0]][loc[1]]
    
    return sum_d


def fucking_block(i,j): # 'ㅗ' 모양 블럭으로 가능한 결과 계산하는 함수
    global nums, max_sum

    # 'ㅗ' 블럭으로 가능한 4가지 경우를 brute-forcely 계산하자
    four_ways = {
                'ㅗ':[(i,j-1),(i,j),(i-1,j),(i,j+1)],
                'ㅓ':[(i,j-1),(i,j),(i-1,j),(i+1,j)],
                'ㅜ':[(i,j-1),(i,j),(i+1,j),(i,j+1)],
                'ㅏ':[(i-1,j),(i,j),(i,j+1),(i+1,j)]
                }

    for locs in four_ways.values():
        calc_valid = True
        for loc in locs:
            if not ( (loc[0] >= 0) and (loc[0] < N) and (loc[1] >= 0) and (loc[1] < M) ): 
                calc_valid = False
                break # 불가능한 좌표있으면 중단
        
        if calc_valid == True: # 계산 가능할 때만 계산
            max_sum = max(max_sum, sum_directly(locs))


# nums의 방문 여부를 표시한 리스트 visited를 reset하는 함수
## -> 사용하지 말자(시간초과)
# def reset_visited():    
#     visited =[]
#     for _ in range(N):
#         visited.append([False for _ in range(M)])
#     return visited

if __name__ == "__main__":
    N,M = tuple(map(int, input().split()))

    nums = [] # N by M 인 정수의 리스트
    for _ in range(N):
        nums.append(list(map(int, input().split())))
    
    visited =[]
    for _ in range(N):
        visited.append([False for _ in range(M)])

    max_sum = 0
    for i in range(N):
        for j in range(M):
            # visited = reset_visited() # -> 사용하지 말자

            visited[i][j] = True # (i,j)를 방문한 상태
            dfs(i,j,1,nums[i][j]) # (i,j)에서부터 dfs 탐색
            fucking_block(i,j) # 'ㅗ' 모양 블럭으로 가능한 결과 계산
            visited[i][j] = False 
            
    print(max_sum)


