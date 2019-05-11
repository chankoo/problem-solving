"""
문제 설명
올바른 괄호란 (())나 ()와 같이 올바르게 모두 닫힌 괄호를 의미합니다. )(나 ())() 와 같은 괄호는 올바르지 않은 괄호가 됩니다. 괄호 쌍의 개수 N이 주어질 때, N개의 괄호 쌍으로 만들 수 있는 모든 가능한 괄호 문자열을 배열형태로 반환하는 함수 solution을 완성해 주세요. 반환되는 문자열 배열은 오름차순으로 정렬되어 있어야 합니다.

제한사항
괄호 쌍의 개수 N : 1 ≤ N ≤ 12, N은 정수

입출력 예
N	result
2	[ (()), ()() ]
3	[ ((())), (()()), (())(), ()(()), ()()() ]

입출력 예 설명
입출력 예 #1
2개의 괄호쌍으로 [ (()), ()() ]의 2가지를 만들 수 있습니다.
입출력 예 #2
3개의 괄호쌍으로 [ ((())), (()()), (())(), ()(()), ()()() ]의 5가지를 만들 수 있습니다.
"""

# sol
# dfs로 올바른 괄호의 케이스를 완전탐색한다

def dfs(lparen, rparen, output, N, answers, visited):

    if lparen == N and rparen == N: # 주어진 괄호를 모두 사용하면 탐색 종료하고 결과에 추가
        answers.append(output)
        return

    for paren in ['(',')']: # 왼괄호와 오른괄호에 대해 탐색 진행
        if paren == '(':
            n_lparen = lparen + 1
            if n_lparen <= N and not visited[n_lparen][rparen]:
                visited[n_lparen][rparen] = True
                dfs(n_lparen, rparen, output+paren, N, answers, visited)
                visited[n_lparen][rparen] = False
            
        elif paren == ')':        
            n_rparen = rparen + 1
            if n_rparen > lparen: # 오른괄호 수가 왼괄호보다 많은 경우 올바르지 않으므로 탐색 종료
                return
            if n_rparen <= N and not visited[lparen][n_rparen]:
                visited[lparen][n_rparen] = True
                dfs(lparen, n_rparen, output+paren, N, answers, visited)
                visited[lparen][n_rparen] = False

def solution(N):
    answers = []
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]
    
    visited[1][0] = True
    dfs(1, 0, '(', N, answers, visited)

    return sorted(answers)

if __name__ == "__main__":
    solution(int(input()))