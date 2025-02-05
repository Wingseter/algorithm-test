#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<int> stk;
    
    for(int i; i < s.length(); i++){
        if(s[i] == '(') {
            stk.push(0);
        }
        else { // )
            if (stk.size() == 0){
                answer = false;
                break;
            }
            stk.pop();
        }
    }
    
    if (stk.size() != 0){
        answer = false;
    }

    return answer;
}