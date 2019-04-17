# https://www.acmicpc.net/problem/17144

# sol
# Map안의 각 요소에 클래스를 담은뒤 시간별 시뮬레이션 진행
# 1) 각 미세먼지의 확산량이 정해져있으므로 이를 브루트 포스하게 계산한다
# 2) 계산값을 집행해 먼지량을 업데이트한다
# 3) 공기청정기로 인한 변화를 적용한다. dfs를 이용한다
# 4) 1)~3)을 반복한다

import sys

class Elem:
    global R, C
    def __init__(self, dust, r, c):
        self.dust = dust
        self.r = r; self.c = c
        self.n_dust = 0
        self.movin = None
        self.visited = False

    def calc_movin(self):  # 자신의 먼지량과 이웃 요소로 확산할 먼지량을 계산
        if self.dust < 5:
            return

        self.movin = self.dust//5  # 이번턴에 확산할 먼지량

        movin_cnt = 0
        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]: # 인접한 칸을 순회하며 확산량 계산
            n_r = r+dr; n_c = c+dc
            if 0<=n_r<R and 0<=n_c<C and Map[n_r][n_c].dust != -1:
                Map[n_r][n_c].n_dust += self.movin
                movin_cnt += 1
        
        self.n_dust -= movin_cnt*self.movin # 확산후 남을 먼지량

    def do_move(self):
        self.dust += self.n_dust
        self.n_dust = 0
        self.movin = None

    def filtering(self, is_upper, filter_r): # 위쪽과 아래쪽의 청정기 규칙이 달라 세부 메소드로 처리한다
        if is_upper:
            self._filtering_upper(filter_r)
        
        else:
            self._filtering_lower(filter_r)

    def _filtering_upper(self, filter_r):
        r = self.r; c = self.c
        # print('r:{}, c:{}'.format(self.r, self.c))
        for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]: # 위쪽 공기청정기 순환의 역순으로 진행한다
            n_r = r+dr; n_c = c+dc
            if (0<=n_r <= filter_r and 0<=n_c<=C-1 ) and ((n_r in (0, filter_r)) or (n_c in (0,C-1))): # 배열을 벗어나지 않으며 위쪽 공기청정기의 영향받는 범위이고
                if n_r <= filter_r and not Map[n_r][n_c].visited: # 아직 dfs 탐색되지 않은 요소일때
                    Map[n_r][n_c].visited = True # 다음 위치의 요소에 방문체크한다
                    
                    if Map[n_r][n_c].dust == -1: # 이때 다음 요소가 공기청정기라면 탐색을 중지한다
                        Map[r][c].dust = 0
                        Map[n_r][n_c].visited = False
                        return

                    Map[r][c].dust = Map[n_r][n_c].dust # 다음 위치의 먼지량을 현재 위치로 땡겨온다
                    Map[n_r][n_c]._filtering_upper(filter_r) # 재귀적으로 진행한다
                    Map[n_r][n_c].visited = False
                    break # 일반적인 탐색과 달리 다음 요소 하나를 찾은 순간 현재 위치에서의 탐색을 종료한다

    def _filtering_lower(self, filter_r):
        r = self.r; c = self.c
        # print('r:{}, c:{}'.format(self.r, self.c))

        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]: # 아래쪽 공기청정기 순환의 역순으로 진행한다
            n_r = r+dr; n_c = c+dc
            if (filter_r<=n_r <= R-1 and 0<=n_c<=C-1 ) and ((n_r in (filter_r, R-1)) or (n_c in (0,C-1))): # 배열을 벗어나지 않으며 아래쪽 공기청정기의 영향받는 범위이고
                if filter_r <= n_r and not Map[n_r][n_c].visited: # 아직 dfs 탐색되지 않은 요소일때
                    Map[n_r][n_c].visited = True # 다음 위치의 요소에 방문체크한다
                    
                    if Map[n_r][n_c].dust == -1: # 이때 다음 요소가 공기청정기라면 탐색을 중지한다
                        # print('청정기는 {}, {}'.format(n_r,n_c))
                        Map[r][c].dust = 0
                        Map[n_r][n_c].visited = False
                        return

                    Map[r][c].dust = Map[n_r][n_c].dust # 다음 위치의 먼지량을 현재 위치로 땡겨온다
                    Map[n_r][n_c]._filtering_lower(filter_r) # 재귀적으로 진행한다
                    Map[n_r][n_c].visited = False
                    break # 일반적인 탐색과 달리 다음 요소 하나를 찾은 순간 현재 위치에서의 탐색을 종료한다


if __name__ == "__main__":
    R, C, T = list(map(int, sys.stdin.readline().split()))
    Map = [[0 for _ in range(C)] for _ in range(R)]
    filter_loc = []

    for r in range(R):
        for c, val in enumerate(map(int, sys.stdin.readline().split())):
            Map[r][c] = Elem(val,r,c)
            if val == -1:
                filter_loc.append((r,c))
            
    t = 0 
    while t<T:
        t += 1

        # calc_movin
        for r in range(R):
            for c in range(C):
                Map[r][c].calc_movin()

        # do_move
        for r in range(R):
            for c in range(C):
                Map[r][c].do_move()

        # filtering
        Map[filter_loc[0][0]-1][filter_loc[0][1]].filtering(is_upper=True,filter_r= filter_loc[0][0])
        Map[filter_loc[1][0]+1][filter_loc[1][1]].filtering(is_upper=False,filter_r= filter_loc[1][0])

    # output
    all_dust = 0
    for r in range(R):
        for c in range(C):
            all_dust += Map[r][c].dust
    print(all_dust+2)

