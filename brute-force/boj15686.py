# https://www.acmicpc.net/problem/15686

# TIL
# itertools 의 사용 -> 순열, 조합 간편하다

import sys
import itertools


class Util:
    @classmethod
    def home_to_chick(cls, h:tuple, comb:list): # 주어진 집과 가장 가까운 치킨집과의 치킨 거리를 반환
        home_dist = 98765
        for chicken in comb:
            home_dist = min(home_dist, abs(h[0]-chicken[0]) + abs(h[1]-chicken[1]) )
        return home_dist


class City:
    n=None
    m=None
    info = []
    home = []
    chicken = []
    min_chick_dist = 987654321

    def __init__(self, n, m):
        self.n = n
        self.m = m

    def fill_info(self):
        for r in range(self.n):
            row = list(map(int, sys.stdin.readline().split()))
            self.info.append(row)
            for c in range(self.n):
                if row[c] == 1:
                    self.home.append((r,c))
                elif row[c] == 2:
                    self.chicken.append((r,c))
    
    def calc_min_dist(self):
        combs = list(itertools.combinations(self.chicken, self.m))
        for comb in combs: # m개 치킨집의 조합 중 하나인 comb에 대해
            this_chicken_dist = 0
            for h in self.home: # home_dist를 계속 더해 해당 comb의 치킨 거리를 구한다
                this_chicken_dist += Util.home_to_chick(h, comb)
            self.min_chick_dist = min(self.min_chick_dist, this_chicken_dist) # min_chick_dist를 갱신한다


if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    city = City(n, m)
    city.fill_info()

    city.calc_min_dist()
    print(city.min_chick_dist)



