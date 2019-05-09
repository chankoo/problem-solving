# https://www.acmicpc.net/problem/1759

# sol
# 주어진 알파벳을 정렬한 후 dfs로 완전탐색한다(크기 작기에 백트랙킹까지 필요하지 않다)
# 탐색은 현재보다 높은 인덱스를 대상으로 진행하며 모음과 자음의 개수를 세면서 조건에 맞을때만 결과에 추가한다


def dfs(pwd, idx, length, mo_cnt, ja_cnt):
    global chars, l, pwds, visited

    if length == l: # 탐색 종료 조건
        if mo_cnt >= 1 and ja_cnt >= 2: # 이용된 모음개수가 1이상, 자음개수가 2이상일때만 결과에 추가
            pwds.append(pwd)

    for i,char in enumerate(chars[idx+1:]):
        if visited[idx+1+i] == False:
            if char in ['a','e','i','o','u']:
                dfs(pwd+char,idx+1+i,length+1,mo_cnt+1,ja_cnt)
            else:
                dfs(pwd+char,idx+1+i,length+1,mo_cnt,ja_cnt+1)


if __name__ == "__main__":
    l,c = tuple(map(int, input().split()))
    chars = sorted(input().split())

    mo_chars = [char for char in chars if char in ['a','e','i','o','u']]
    za_chars = [char for char in chars if char not in ['a','e','i','o','u']]

    pwds = []
    visited = [False for _ in chars]
    for start in range(c-l+1):
        visited[start] = True
        if chars[start] in mo_chars:
            dfs(chars[start],start,1,1,0)
        else:
            dfs(chars[start],start,1,0,1)
        visited[start] = False

    for pwd in sorted(pwds):
        print(pwd)