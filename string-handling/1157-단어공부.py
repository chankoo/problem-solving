# https://www.acmicpc.net/problem/1157

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

S = input().lower()
abc = dict.fromkeys([chr(i) for i in range(97,123)],0)

for s in S:
    abc[s]+=1

vals = list(abc.values())
maxVal=max(vals)
if vals.count(maxVal)>1:
    print('?')
else:
    for item in abc.items():
        if item[1]==maxVal:
            print(item[0].upper())