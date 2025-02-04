#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> counter;
    
    for (auto partici : participant){
        counter[partici] += 1;
    }
    
    for (auto comple : completion) {
        counter[comple] -= 1;
    }
    
    for (auto& it: counter) {
        if (it.second != 0) {
            answer = it.first;
        }
    }
    return answer;
}