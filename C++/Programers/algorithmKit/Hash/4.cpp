// 결국 모든 경우의 수는 각각의 경우의 수를 곱한 것과 같다.
#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 0;
    if(clothes.size() == 0) return 0;
    
    unordered_map<string, int> collect;
    
    for (auto cloth : clothes) {
        string categories = cloth[1];
        collect[categories] += 1;
    }
    
    answer = 1;
    for (auto& value : collect){
        answer *= (value.second + 1);
    }
    answer -= 1;
    
    return answer;
}