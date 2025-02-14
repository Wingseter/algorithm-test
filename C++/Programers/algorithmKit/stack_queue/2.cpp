// 미리 필요한 숫자를 구할 수 있었다. 이게 훨씬 편했다.
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <math.h>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    
    for(int i = 0; i < progresses.size(); i++) {
        q.push(ceil((100.0 - progresses[i]) / speeds[i]));
    }
    
   int biggest = -987654321;
    
    while(!q.empty())
    {
        int front = q.front();
        if (front > biggest) {
            biggest = front;
            answer.push_back(1);
        }
        else {
            answer.back() += 1;
        }
        q.pop();
    }
    
    return answer;
}