# https://www.acmicpc.net/problem/1753

# sol
# (1≤V≤20,000, 1≤E≤300,000) 이므로 시간, 메모리 관리 필요
# 벨만포드[O(VE) = 60억], 플로이드[O(V^3) = 8조] 사용 불가
# 다익스트라 이용
# 인접행렬로 풀이불가( O(V^2), 메모리초과 ). 인접 리스트(adjlst)를 사용
# PriorityQueue를 이용해 최단거리 정점을 확보하는 것이 핵심
# pq에 넣는 거리는 시작점으로부터의 최단거리
# 현재 이코드로도 시간초과됨. 거의 같은 논리의 코드가 통과하는걸로 봐서는 파이썬이 느린탓인듯

import sys
from queue import PriorityQueue
print = sys.stdout.write
INF = 1e9

def get_adjlst(v,e):
    adjlst = [[] for _ in range(v+1)] # adjlst를 초기화

    for _ in range(e):
        u, v, w = tuple(map(int, sys.stdin.readline().split()))
        adjlst[u].append( (w, v) ) # edge u->v 를 표현하는 (cost, vertex) 형태로 adjlst를 완성
    return adjlst

def dijkstra(adjlst, k):
    V = len(adjlst)-1 # 정점의 개수
    dists = [INF for _ in range(V+1)] # 정점과의 최단거리 담을 dist 배열

    pq = PriorityQueue(maxsize=V) # k로 부터의 최단거리 순으로 정점을 반환할 우선순위큐 초기화
    pq.put((0,k)) # 시작점의 거리는 0
    dists[k] = 0 
    determined = [] # 최단거리가 확정된 정점들을 담을 배열

    while not pq.empty():
        dist, v = pq.get() # 현재 k로 부터의 최단거리를 확보한 정점과 그 최단거리
        determined.append(v) # 최단거리 확정된 정점임을 명시

        if dist > dists[v]: # 아래 과정에서 한 정점 v에 대해 pq에 저장된 최단거리가 여러개이므로 불필요한 계산은 continue
            continue

        for n_w, n_v in adjlst[v]:
            if n_v in determined: # 다음 정점 후보가 이미 최단거리 확정된 정점이라면 continue
                continue
            
            if dists[v] + n_w < dists[n_v]: # 다음 정점 후보가 해당 정점에 대한 최단거리를 갱신한다면
                dists[n_v] = dists[v] + n_w # 최단거리를 업데이트하고
                pq.put((dists[n_v], n_v)) # pq에 후보로 push


    # 각 정점으로의 최단 경로값 출력
    for dist in dists[1:]:
        print("%d\n" % dist if dist != INF else "INF\n")
    return


if __name__ == "__main__":
    V,E = tuple(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    adjlst = get_adjlst(V,E)
    dijkstra(adjlst, k)