# https://www.acmicpc.net/problem/1931

# sol
# 최대한 많이 job을 수행하려면 끝나는 시간 오름차순으로 정렬하여 배치한다
# 이때, 시작 시간과 종료 시간이 동일한 job의 경우 제한없이 수행가능하다는 조건을 고려하고
# 종료 시간이 같다면 시작하는 시간이 빠른 순으로 배치하면 
# (3,3), (2,3), (3,3)과 같은 jobs가 주어졌을때 올바른 답(3)을 낼 수 있다

import sys
from collections import deque

if __name__ == "__main__":
    N = int(input())

    jobs = []
    for _ in range(N):
        s, e = sys.stdin.readline().rstrip('\n').split()
        jobs.append( (int(s), int(e)) )
    
    jobs = sorted(jobs, key = lambda tup:tup[0])
    jobs = deque(sorted(jobs, key = lambda tup:tup[1]))
    selected = None
    job_cnt = 0
    while len(jobs) > 0:
        tmp_job = jobs.popleft()
        if tmp_job[1] - tmp_job[0] == 0:
            selected = tmp_job
            job_cnt += 1
            continue
        if selected is not None:
            if tmp_job[0] < selected[1]:
                continue
        selected = tmp_job
        job_cnt += 1

    print(job_cnt)