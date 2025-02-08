#include <string>
#include <vector>
#include <climits>

using namespace std;


int total_max_visit = 0;
void permutation(int power, int max_visit, vector<vector<int>>& dungeons, vector<bool>& visited) {
    total_max_visit = max(total_max_visit, max_visit);
    
    if (dungeons.size() == max_visit) return;
    
    for(int i = 0; i < dungeons.size(); i++) {
        if (power >= dungeons[i][0])
            if(!visited[i]) {
                visited[i] = true;
                permutation(power - dungeons[i][1], max_visit + 1, dungeons, visited);
                visited[i] = false;
            }
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    vector<bool> visited(dungeons.size(), false);
    
    permutation(k, 0,  dungeons, visited);
    
    answer = total_max_visit;
    return answer;
}