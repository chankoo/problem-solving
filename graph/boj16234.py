# https://www.acmicpc.net/problem/16234

# sol
# Country 클래스를 이용하여 bfs와 브루트 포스로 어렵지 않게 구현한다
# Country의 클래스 변수 union_set에 Country 인스턴스를 저장하는 것이 핵심
# 1) 연합을 구성한다
#   1-1) 각 점에서의 bfs를 반복하여 각각의 연합을 구성한다
#   1-2) 다른 연합에 중복으로 속하지 않기에 이부분을 검색에서 제외하여 완전탐색의 비효율을 줄인다
# 2) 연합간의 인구 이동을 진행한다
#   2-1) union_set에 매핑된 {연합번호: [Country 인스턴스들]}을 이용한다
# 3) 연합을 해제하고 인스턴스의 연합 관련 변수를 초기화한다
# 4) 연합구성 안될때까지 1~3)을 반복한다

import sys
from collections import deque

class Country:
    union_set = {}
    def __init__(self, pop, is_union=False):
        self.pop = pop
        self.is_union = is_union
    
    @classmethod
    def reset_union(cls):
        for union in cls.union_set.values():
            for country in union:
                country.is_union = False
        cls.union_set = {}

def bfs_set_union(init_r,init_c):
    global Map, N, L, R, visited
    if Map[init_r][init_c].is_union: # 이미 소속된 union이 있다면 탐색이 불필요하다
        return

    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    q = deque([])
    q.append((init_r,init_c))
    visited[init_r][init_c] = 1
    
    union_lst = []
    union_lst.append(Map[init_r][init_c])
    Map[init_r][init_c].is_union = True
    while len(q) > 0:
        r,c = q.popleft()
        pop = Map[r][c].pop

        for mv in moves:
            n_r = r+mv[0]
            n_c = c+mv[1]
            if 0 <= n_r < N and 0 <= n_c < N:
                n_pop = Map[n_r][n_c].pop
                # union을 이룰 조건 만족할 경우는 아래와 같다
                if not Map[n_r][n_c].is_union and L <= abs(n_pop-pop) <= R and visited[n_r][n_c] == 0:
                    union_lst.append(Map[n_r][n_c])
                    q.append((n_r,n_c))
                    visited[n_r][n_c] = 1
                    Map[n_r][n_c].is_union = True
    
    if len(union_lst) < 2: # init_r, init_c 점에서 시작한 연합이 구성되지 않았다면 시작점의 마킹을 해제
        Map[init_r][init_c].is_union = False
    
    else: # 연합 구성되었다면 연합번호를 부여하고 Country 클래스 변수에 추가
        max_key = max(list(Country.union_set.keys()) + [-1])
        Country.union_set[max_key+1] = union_lst

    return

def pop_move():
    for union in Country.union_set.values():
        union_pop = 0
        country_num = len(union)
        
        for country in union:
            union_pop += country.pop
        for country in union:
            country.pop = union_pop//country_num


if __name__ == "__main__":
    N, L, R = tuple(map(int, sys.stdin.readline().split()))
    Map = [[None for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c, pop in enumerate(list(map(int,sys.stdin.readline().split()))):
            Map[r][c] = Country(pop)

    move_num = 0
    while True:
        # 연합을 구성한다
        visited = [[0 for _ in range(N)] for _ in range(N)]
        for r in range(N):
            for c in range(N):
                # print('r,c = {},{}'.format(r,c))
                bfs_set_union(r,c)

        # 연합이 만들어지지 않으면 인구이동이 발생하지 않는다
        if Country.union_set == {}:
            break

        # 인구 이동이 발생한다
        pop_move()
        move_num += 1
        
        # 연합을 해제한다
        Country.reset_union()

    print(move_num)