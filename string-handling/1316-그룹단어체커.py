# https://www.acmicpc.net/problem/1316

# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

def isGroup(s):
    abc = dict.fromkeys([chr(i) for i in range(97,123)],0)
    for i in range(len(s)):
        if abc[s[i]]==0: # 첫번째 등장 체크
            abc[s[i]]=1
        elif (abc[s[i]]==1 and s[i]==s[i-1]): # 연속해서 등장하는 경우
            pass
        elif (abc[s[i]]==1 and s[i]!=s[i-1]): # 연속하지 않고 등장하는 경우
            abc[s[i]]=2
        else:pass
    if 2 in list(abc.values()):
        return 0
    return 1

N = int(input())
count=0
for i in range(N):
    s = input()
    if isGroup(s)==1:
        count+=1

print(count)