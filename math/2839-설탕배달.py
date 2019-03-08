# https://www.acmicpc.net/problem/2839

# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

N = int(input())

count3=0 # 3kg 봉지 사용 개수
count5=0 # 5kg 봉지 사용 개수
count5 = N//5 # 우선 가능한 5kg 봉지 모두 사용

if count5>0: # 5kg 사용 가능했다면 남은 N
    N=N%5 

if N%3==0: # 남은 N이 3으로 나눠떨어진다면 그대로 출력
    count3 = N//3
    print(count3+count5)

elif N%3==1: # 남은 N을 3으로 나눴을때 나머지 1이면
    if count5>0: 
        count5-=1 # 5kg 봉지 하나를 줄이면 3kg 봉지로 커버 가능
        N+=5
        count3 = N//3
        print(count3+count5)
    else:
        print(-1)

elif N%3==2: # 남은 N을 3으로 나눴을때 나머지 2이면
    if count5>1: 
        count5-=2 # 5kg 봉지 2개를 줄이면 커버가능
        N+=10
        count3 = N//3
        print(count3+count5)
    else:
        print(-1)
        
    
