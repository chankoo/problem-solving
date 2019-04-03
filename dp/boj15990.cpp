// # https://www.acmicpc.net/problem/15990

// # sol
// # boj15989 1,2,3 더하기 4와 유사한 풀이다
// # 정수 i를 만드는 경우의 수를 각각 1,2,3으로 시작한 case로 분류하고 
// # 2차원 배열 mem에 쌓아나간다
// # 이때, mem[i][0] = mem[i-1][1] + mem[i-1][2] 로 표현가능하다
// # i를 1로 시작해서 만드는 case구하는 것이고, 이는 i-1을 2로 시작해 만든 case와 3으로 시작해 만든 case의 합이기 때문이다
// TIL
// overflow 조심

#include <iostream>
#include <string>
#include <deque>
#define MOD 1000000009
using namespace std;

int case_cnt(int n){
	deque<deque<int> > mem;
	int sum = 0;

	// initiating base cases
	deque<int> temp;
	temp.push_back(1);temp.push_back(0);temp.push_back(0); // n==1, case: (1)
    mem.push_back(temp); 
    temp.clear();
    
    temp.push_back(0);temp.push_back(1);temp.push_back(0); // n==2, case: (2)
	mem.push_back(temp); 
	temp.clear();
    
	temp.push_back(1);temp.push_back(1);temp.push_back(1); // n==3, case: (1+2, 2+1, 3)
    mem.push_back(temp); 
    temp.clear();
    
    if(n < 4){
		for(int i=0;i<3;i++){
			sum = sum + mem[n-1][i];
		}
		return sum;
	}
	
	for(int r=3;r<n;r++){
		deque<int> this_val;
		this_val.push_back( (mem[2][1]+mem[2][2]) % MOD); // of cases make row begin with 1
		this_val.push_back( (mem[1][0]+mem[1][2]) % MOD); // of cases make row begin with 2
		this_val.push_back( (mem[0][0]+mem[0][1]) % MOD); // of cases make row begin with 3
		
		mem.push_back(this_val);
		mem.pop_front(); // delete old memory
	}
	for(int i=0;i<3;i++){
		sum = (sum + mem[2][i]) % MOD;
	}
	return sum % MOD;
}

int main(){
    int t;
    cin >> t;

    for(int i=0;i<t;i++){
        int n;
        cin >> n; 
        cout << case_cnt(n) << endl;
    }
    return 0;
}
