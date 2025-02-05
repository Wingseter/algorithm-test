#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    
    queue<pair<int, int>> q; 
    priority_queue<int> pq;
    
    for (int i = 0; i < priorities.size(); i++) {
        q.push({priorities[i], i});  
        pq.push(priorities[i]);      
    }
    
    int counter = 1;
    while(!q.empty()) {
        int prior = q.front().first;
        int idx = q.front().second;
        
        q.pop();
        if (prior != pq.top()) {
            q.push({prior, idx});
        }
        else {
            priorities[idx] = counter;
            counter += 1;
            pq.pop();
        }
    }
    
    answer = priorities[location];
    return answer;
}