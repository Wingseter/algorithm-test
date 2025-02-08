#include <string>
#include <vector>
#include <queue>

using namespace std;

bool is_this_two_pair(string w1, string w2) {
    int length = w1.size();
    
    int count = 0;
    for(int i = 0; i < length; i++) {
        if(w1[i] != w2[i]) {  
            count += 1;
        }
    }
    return count == 1;  
}

int search(string begin, string target, vector<string> words, vector<bool> visited) {
    queue<pair<string, int>> q;
    q.push({begin, 0});
    
    while(!q.empty()) {
        auto word_value = q.front();
        string wordstart = word_value.first;
        int count = word_value.second;
        q.pop();
        
        for(int i = 0; i < words.size(); i++) {
            if(!visited[i] && is_this_two_pair(wordstart, words[i])) { 
                if (words[i] == target) {
                    return count + 1;
                }
                visited[i] = true;
                q.push({words[i], count + 1});
            }
        }
    }
    return 0; 
}

int solution(string begin, string target, vector<string> words) {
    vector<bool> visited(words.size(), false);
    return search(begin, target, words, visited);
}
