#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    
    unordered_set<string> set;
    
    for (auto phone : phone_book){
        set.insert(phone);
    }
    
    for (auto phone: phone_book){
        for (int i = 0; i < phone.length(); i ++){
            if(set.count(phone.substr(0, i))){
                answer = false;
                break;
            }
        }
        if (answer == false) break;
    }
    return answer;
}