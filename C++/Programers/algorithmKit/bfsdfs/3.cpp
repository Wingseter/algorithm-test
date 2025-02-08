#include <vector>
#include <queue>
#include <iostream>

using namespace std;

vector<int> dy = {0, 1, 0 , -1};
vector<int> dx = {1, 0, -1, 0};

void search(vector<vector<int>>& maps, vector<vector<int>>& visited) 
{
    queue<pair<int, int>> q;
    q.push({0, 0});
    visited[0][0] = 1;
    
    while(!q.empty()) {
        auto p = q.front();
        int y = p.first;
        int x = p.second;
        q.pop();
        
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            // dont move if out of maps
            if (ny < 0 || ny >= maps.size() || nx < 0 || nx >= maps[0].size()) {
                continue;
            }
            
            if (visited[ny][nx] == 0 && maps[ny][nx] == 1) {
                q.push({ny, nx});
                visited[ny][nx] = visited[y][x] + 1;
            }
        }
    }
}

int solution(vector<vector<int>> maps)
{
    int answer = 0;
    vector<vector<int>> visited(maps.size(), vector<int>(maps[0].size(), 0));
    
    search(maps, visited);
    
    answer = visited[maps.size() - 1][maps[0].size() - 1];
    if (visited[maps.size() - 1][maps[0].size() - 1]  == 0) answer = -1;
    
    return answer;
}