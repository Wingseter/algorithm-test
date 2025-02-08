#include <string>
#include <vector>
#include <queue>
#include <climits>
#include <cmath>
#include <iostream>

using namespace std;

int count_node(int start_node, vector<vector<int>>& graph, vector<bool> visited) {
    int counter = 1;
    queue<int> q;
    visited[start_node] = true;
    q.push(start_node);
    
    while(!q.empty()) {
        int select_node = q.front();
        q.pop();
        
        for(int node = 0; node < graph.size(); node++ ) {
            if(graph[select_node][node] == 1){
                if(!visited[node]) {
                    q.push(node);
                    visited[node] = true;
                    counter += 1;
                }
            }
        }
    }
    return counter;
}

int solution(int n, vector<vector<int>> wires) {
    int answer = -1;
    
    vector<vector<int>> graph(n + 1, vector<int>(n + 1, 0));
    vector<bool> visited(n + 1, false);
    
    for (auto wire : wires) {
        int a = wire[0];
        int b = wire[1];
        
        graph[a][b] = 1;
        graph[b][a] = 1;
    }
    
    int minimum_diff = INT_MAX;
    for(int i = 0; i < wires.size(); i++) {
        int a = wires[i][0];
        int b = wires[i][1];
        
        graph[a][b] = 0;
        graph[b][a] = 0;
        
        int sel_a = count_node(1, graph, visited);
        int sel_b = n - sel_a;
        
        graph[a][b] = 1;
        graph[b][a] = 1;
        
        minimum_diff = min(minimum_diff, abs(sel_a - sel_b));
    }

    answer = minimum_diff;
    
    return answer;
}