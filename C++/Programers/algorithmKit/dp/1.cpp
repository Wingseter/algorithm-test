#include <iostream>
#include <vector>
#include <set>
#include <climits>

using namespace std;

int solution(int N, int number) {
    vector<set<int>> dp(9);  

    dp[1].insert(N);
    
    for (int i = 2; i <= 8; i++) {
        for (int j = 1; j < i; j++) {
            for (int x : dp[j]) {
                for (int y : dp[i - j]) {
                    dp[i].insert(x + y);  
                    dp[i].insert(x - y);  
                    dp[i].insert(x * y);  
                    if (y != 0) {
                        dp[i].insert(x / y); 
                    }
                }
            }
        }
        

        int num = 0;
        for (int j = 0; j < i; j++) {
            num = num * 10 + N;  
        }
        dp[i].insert(num);
    }   

    for (int i = 1; i <= 8; i++) {
        if (dp[i].count(number)) {
            return i;
        }
    }
    
    return -1;
}

