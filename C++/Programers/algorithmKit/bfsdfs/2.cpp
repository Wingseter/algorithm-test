#include <string>
#include <vector>

using namespace std;

void dfs(vector<vector<int>>& computers, vector<bool>& visited, int select){
    if(visited[select]) {
       return; 
    }
    visited[select] = true;
    
    for(int i = 0; i < computers[select].size(); i++) {
        if(computers[select][i] == 1) {
            dfs(computers, visited, i);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    int network_count = 0;
    vector<bool> visited(computers.size(), false);
    for(int select = 0; select < computers.size(); select++) {
        if(!visited[select]) {
            dfs(computers, visited, select);
            network_count += 1;
        }
    }
    answer = network_count;
    return answer;
}