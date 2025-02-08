#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    for(int i = 1; i <= yellow; i++) {
        if (yellow % i == 0) {
            int yellow_h = i;
            int yellow_w = int(yellow / yellow_h);
            
            if (((yellow_h + 2) * 2 + (yellow_w + 2) * 2 - 4) == brown) {
                answer.push_back(yellow_w + 2);
                answer.push_back(yellow_h + 2);
                
                break;
            }
        }
    }
    return answer;
}