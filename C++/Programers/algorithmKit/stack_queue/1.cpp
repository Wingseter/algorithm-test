#include <vector>
#include <iostream>
#include <stack>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    std::stack<int> stk;
    
    
    answer.push_back(arr[0]);
    for(int num: arr){
        if (answer.back() != num){
            answer.push_back(num);
        }
    }

    return answer;
}