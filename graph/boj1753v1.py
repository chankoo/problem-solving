# https://www.acmicpc.net/problem/1753

# sol
# (1≤V≤20,000, 1≤E≤300,000) 이므로 시간, 메모리 관리 필요
# 벨만포드[O(VE) = 60억], 플로이드[O(V^3) = 8조] 사용 불가
# 다익스트라 이용
# 인접행렬로 풀이 역시 어려운 문제. 결과는 O(V^2), 메모리초과

import sys

def get_adjmat(v,e):
    adjmat = [[float('inf') for _ in range(v)] for _ in range(v)]
    for _ in range(e):
        u, v, w = tuple(map(int, sys.stdin.readline().split()))
        
        # 정점간 여러개의 edge 존재 가능하므로 최솟값을 입력
        if w < adjmat[u-1][v-1]:
            adjmat[u-1][v-1] = w
    return adjmat

def dijkstra(adjmat, k):
    min_dist_arr = adjmat[k-1] # k로 부터의 최단거리를 저장할 배열
    determined = [k, ] # 최단거리가 확정된 vertices
    adjmat[k-1][k-1] = 0

    while len(determined) < len(adjmat):
        next_v = None
        next_w = float('inf')
        for v_i, w in enumerate(min_dist_arr):
            v = v_i + 1
            if v not in determined and w < next_w: # 최단거리 확정안된 정점 중 k와 거리 가장 가까운점 
                next_v = v
                next_w = w
        if next_v is None:
            break

        determined.append(next_v) # 해당 정점까지의 최단거리 확정(greedy하게)
        # print(determined)
        v = next_v # 최단거리가 확정된 정점을 기준으로 
        for next_v_i, next_w in enumerate(adjmat[v-1]): # min_dist_arr를 업데이트
            if next_w != float('inf'):
                min_dist_arr[next_v_i] = min(min_dist_arr[next_v_i], adjmat[k-1][v-1] + next_w)

    for dist in min_dist_arr:
        if dist == float('inf'):
            print('INF')
            continue
        print(dist)

    return

if __name__ == "__main__":
    V,E = tuple(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    adjmat = get_adjmat(V,E)
    dijkstra(adjmat, k)