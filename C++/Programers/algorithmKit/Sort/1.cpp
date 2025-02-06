#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(auto command : commands) {  
        int start = command[0] - 1;
        int end = command[1];
        int point = command[2];
        
        vector<int> sub(array.begin() + start, array.begin() + end);
        sort(sub.begin(), sub.end());
        answer.push_back(sub[point - 1]);
    }
    
    
    return answer;
}