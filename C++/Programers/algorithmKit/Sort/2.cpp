#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    
    vector<string> str_num;
    
    for (int number : numbers) {
        str_num.push_back(to_string(number));
    }
    
    // 이 정렬 방식을 기억하자 람다를 이용한 방법이다.
    sort(str_num.begin(), str_num.end(), [](const string &a, const string &b) {
        return a + b > b + a;
    });
    
    if (str_num[0] == "0") return "0";
    
    for (string s: str_num) {
        answer += s;
    }
    return answer;
}