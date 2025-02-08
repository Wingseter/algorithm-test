#include <string>
#include <vector>
#include <iostream>
#include <unordered_set>

using namespace std;
unordered_set<int> set;

bool is_sosu(int num) {
    bool sosu = true;
    if (num == 0 || num == 1) 
        return false;
    
    for(int i = 2; i < num - 1; i ++ ) {
        if (num % i == 0) {
            sosu = false;
            break;
        }
    }
    return sosu;
}

void permutation(int n, string st, string numbers, vector<bool> visited)
{
    if(!st.empty()) set.insert(stoi(st));
    
    for(int i = 0; i < n; i++ ) {
        if(!visited[i]) {
            visited[i] = true;
            permutation(n, st + numbers[i], numbers, visited);
            visited[i] = false; 
        }
    }
}

int solution(string numbers) {
    int answer = 0;
    set.clear();
    vector<bool> visited(numbers.size(), false);
    permutation(numbers.size(), "", numbers, visited);
    
    for(auto k: set) {
        if (is_sosu(k))
        {
            answer += 1;
        }
        cout << k << " ";
    }
    return answer;
}