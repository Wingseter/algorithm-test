#include <string>
#include <vector>
#include <stack>

using namespace std;

int total_sum;

void dfs(vector<int> numbers, int target, int index, int plus) {
    if(index == numbers.size()) {
        if (plus == target) {
            total_sum += 1;
        }
        return;
    }

    dfs(numbers, target, index + 1, plus + numbers[index]);
    dfs(numbers, target, index + 1, plus - numbers[index]);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    total_sum = 0;
    dfs(numbers, target, 0, 0);
    answer = total_sum;
    
    return answer;
}