#include <vector>
#include <unordered_set>
#include <iostream>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int length = nums.size();
    
    unordered_set<int> set;
    for(int num: nums){
        set.insert(num);
    }
    int element = set.size();
    
    answer = min(element, int(length / 2));
    return answer;
}