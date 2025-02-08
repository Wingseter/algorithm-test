#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<vector<int>> rules = {
        {1, 2, 3, 4, 5},
        {2, 1, 2, 3, 2, 4, 2, 5},
        {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
    };
    
    int answer_size = answers.size();
    vector<int> correct(3, 0);
    for(int i = 0; i < rules.size(); i++) {
        int answer_pt = 0;
        int rules_pt = 0;
        
        for (int j = 0; j < answer_size; j++) {
            if(answers[answer_pt] == rules[i][rules_pt]) {
                correct[i] += 1;
            }
            answer_pt = (answer_pt + 1) % answer_size;
            rules_pt = (rules_pt + 1) % rules[i].size();
        }
    }
    
    int max_score = *max_element(correct.begin(), correct.end());
    for(int i = 0; i < rules.size(); i++) {
        if (correct[i] == max_score) {
            answer.push_back(i + 1);
        }
    }
    return answer;
}