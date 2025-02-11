// 0 과 마지막에서 각각 한쪽만 구해야 했다. 아니면 오류가 발생한다.
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> cloth(n, 1);
    
    for(int lost_each: lost) {
        cloth[lost_each- 1] -= 1;
    }
    for(int res_each: reserve) {
        cloth[res_each - 1] += 1;
    }
    
    if(cloth[0] == 2 && cloth[1] == 0) {
        cloth[0] = 1;
        cloth[1] = 1;
    }
    if(cloth[n - 1] == 2 && cloth[n - 2] == 0) {
        cloth[n - 1] = 1;
        cloth[n - 2] = 1;
    }
    
    for(int i = 1; i < n -1; i++) {
        if(cloth[i] == 2) {
           if(cloth[i - 1] == 0) {
               cloth[i] = 1;
               cloth[i- 1] = 1;
            }
            else if (cloth[i + 1] == 0) {
                cloth[i] = 1;
                cloth[i + 1] = 1;
            }
        }
    }
    
    for(int i = 0; i < n; i++) {
        if (cloth[i] > 0) {
            answer += 1;
        }
    }

    return answer;
}
