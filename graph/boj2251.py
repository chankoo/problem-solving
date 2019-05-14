# https://www.acmicpc.net/problem/2251

# sol
# 물통의 수가 3개 뿐이고 가능한 경우의 수가 많지 않으므로 dfs로 풀었다
# 가능한 물통들의 상태를 status 배열로 만들고 이 배열 자체로 방문체크를 하였다(멤버쉽 연산 이용)
# 이때 mutable 타입은 멤버쉽 연산이 가능한 key로 hash될 수 없기에 visited에 넣을땐 tuple로 변환하였다

def pour(_from, _to, status):
    global V
    if status[_from] > 0:
        n_status = [*status]
        
        if V[_to] - status[_to] == 0:
            return status

        else:
            if V[_to] - status[_to] >= status[_from]:
                n_status[_to] = status[_to] + status[_from]
                n_status[_from] = 0

            else:
                n_status[_to] = V[_to]
                n_status[_from] = n_status[_from] - (V[_to] - status[_to])
        return n_status

    return status

def dfs(status):
    global visited, output

    if status[0] == 0:
        output.append(status[2])

    for _from,_to in [(0,1),(0,2),(1,2),(1,0),(2,0),(2,1)]:
        n_status = tuple(pour(_from, _to, status))
        if n_status not in visited:
            visited.add(n_status)
            dfs(n_status)


if __name__ == "__main__":
    V = tuple(map(int, input().split()))

    visited = set()
    output = []

    status = [0,0,V[2]]
    visited.add(tuple(status))

    dfs(status)

    for vol in sorted(output)[:-1]:
        print(vol, end=' ')
    print(sorted(output)[-1])