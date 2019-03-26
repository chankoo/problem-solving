// # https://www.acmicpc.net/problem/15990

// # sol
// # boj15989 1,2,3 더하기 4와 유사한 풀이다
// # 정수 i를 만드는 경우의 수를 각각 1,2,3으로 시작한 case로 분류하고 
// # 2차원 배열 mem에 쌓아나간다
// # 이때, mem[i][0] = mem[i-1][1] + mem[i-1][2] 로 표현가능하다
// # i를 1로 시작해서 만드는 case구하는 것이고, 이는 i-1을 2로 시작해 만든 case와 3으로 시작해 만든 case의 합이기 때문이다
// # 메모리 문제 때문에 cache 배열을 구현

#include <iostream>
#include <string>

using namespace std;

int case_cnt(int n){

    return n;
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
