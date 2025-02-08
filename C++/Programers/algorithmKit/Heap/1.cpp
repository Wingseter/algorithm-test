#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    // 이 방식을 기억하지 pq 선언 방법 단 큰 순서대로 정렬
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for(int scov : scoville) {
        pq.push(scov);
    }
    

    int first, second, new_food;
    while(pq.size() > 1) {
       if (pq.top() >= K) {
            return answer;
        }
        
        first = pq.top();
        pq.pop();
        second = pq.top();
        pq.pop();
        
        new_food = first + second * 2;
        
        answer += 1;
        pq.push(new_food);
        
    }
    
    if (pq.top() < K) answer = -1;

    return answer;
}