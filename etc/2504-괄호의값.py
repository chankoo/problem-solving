# https://www.acmicpc.net/problem/2504

from collections import deque,Counter

def to_infix(data:str): # 괄호로 표현된 수식을 일반적인 infix 표현으로 바꾼다
    c = Counter(data)
    global lst # infix 표현 저장할 리스트

    most_count = c.most_common(1)[0][1] # 가장 freq 높은 괄호의 cnt
    if  c['('] != c[')'] or c['['] != c[']']: # (),[] 짝이 맞지 않다면
        return 0
    
    for par in data:
        if par in lpar: # '(' ,'[' 왼쪽 괄호는 일단 저장
            lst.append(par)

        else: # 오른쪽 괄호의 경우에는 case 나누어 값과 함께 저장
            if par==']': 
                if lst[-1] in rpar: # case [[]], [()]
                    lst.extend(['*','3',']'])
                elif lst[-1] =='[': # case []
                    lst.extend(['3',']'])
                else:
                    return 0
            elif par==')':
                if lst[-1] in rpar: # case (()), ([])
                    lst.extend(['*','2',')'])
                elif lst[-1] == '(': # case ()
                    lst.extend(['2',')'])
                else:
                    return 0
    
    # 저장된 결과값의 처리
    res = ''.join(lst) 
    res = res.replace('[','(').replace(']',')')
    res = res.replace(')(','+')
    
    return res

# Calculator 클래스 구현해서 계산해보자
# 참고 https://wayhome25.github.io/cs/2017/04/18/cs-22/
class Calculator:
    def __init__(self,infix):
        self.infix = infix
        self.postfix = None
        
    def get_weight(self, oprt): # 연산자의 우선 순위를 지정한다
        if oprt == '*' or oprt == '/':
            return 9
        elif oprt == '+' or oprt == '-':
            return 7
        elif oprt == '(':
            return 5
        else:
            return -1
    
    def to_postfix(self): # 구현의 핵심
        oprt_stack = [] # 연산자 저장위한 스택
        exp_q = deque() # 후위표현식 저장위한 큐

        for ch in self.infix:
            if ch=='(': # 왼쪽 괄호는 push
                oprt_stack.append(ch)

            elif ch==')': # 오른쪽 괄호 만나면 짝맞는 왼쪽 괄호 만날때까지 스택에서 pop
                while oprt_stack!=[]:
                    poped = oprt_stack.pop()
                    if poped =='(':
                        break
                    exp_q.append(poped)

            elif ch in [str(el) for el in range(10)]: # 숫자들어온 경우
                exp_q.append(ch)
                
            else: # 연산자 들어온경우
                if oprt_stack == []:
                    oprt_stack.append(ch)
                elif self.get_weight(ch) > self.get_weight(oprt_stack[-1]): # 들어온 연산자의 가중치가 높을때 -> 들어온 연산자 push
                    oprt_stack.append(ch)
                else: # 들어온 연산자의 가중치가 낮거나 같을때 -> 스택의 연산자들 우선 pop(기존 연산자 우선 계산에 포함)
                    while oprt_stack!=[] and self.get_weight(ch) <= self.get_weight(oprt_stack[-1]):
                        exp_q.append(oprt_stack.pop())
                    oprt_stack.append(ch)
        
        while oprt_stack !=[]:
            exp_q.append(oprt_stack.pop()) 
        self.postfix = ''.join(exp_q) # 후위 표현식 완성
        
    def calc_two_oprd(self, oprd1, oprd2, oprt):
        if oprt == '+':
            return oprd1 + oprd2
        elif oprt == '-':
            return oprd1 - oprd2
        elif oprt == '*':
            return oprd1 * oprd2
        elif oprt == '/':
            return oprd1 // oprd2

    def calc_postfix(self):
        oprd_stack = [] # 피연산자 저장위한 스택

        for ch in self.postfix:
            if ch in [str(el) for el in range(10)]: # ch가 숫자
                oprd_stack.append(int(ch))
            else: # ch가 연산자면 피연산자 스택에서 뽑아서 해당 연산자로 연산
                oprd2 = oprd_stack.pop()
                oprd1 = oprd_stack.pop()
                oprd_stack.append(self.calc_two_oprd(oprd1,oprd2,ch))

        return oprd_stack.pop()

if __name__=="__main__":
    data = input()
    lst = []
    rpar = [']',')']
    lpar = ['[','(']
    
    infix = to_infix(data)
    
    calc = Calculator(infix) # Calculator 생성
    try:
        calc.to_postfix() # postfix로 바꾼 후
        print(calc.calc_postfix()) # 연산한 값 print
    except Exception:
        print(0)