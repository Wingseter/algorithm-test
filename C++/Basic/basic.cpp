#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
    // int n = 7, m = 8;

    // vector<int> nums1;
    // vector<int> nums2(n);
    // vector<int> nums3{1, 3, 5};
    // vector<int> nums4(n, 2);
    // vector<vector<int>> dp;
    // vector<vector<bool>> dp(m, vector<bool>(n, true));

    // nums1.empty();
    // nums2.size();
    // nums3.back();
    // nums4.push_back(3);
    // nums4.pop_back();
    int n = 10;

    vector<int> nums(n);

    cout << nums.empty();
    cout << nums.size();
    int a = nums[4];
    nums.push_back(20);

    cout << nums.size();
    int b = nums.back();
    cout << b;

    nums.pop_back();
    cout << nums.size();

    swap(nums[0], nums[1]);

    string s;
    s = "abcd";

    cout << s[2];
    s.push_back('e');

    cout << s;
    cout << s.substr(2, 3);
    s += "xyz";
    cout << s;

    unordered_map<int, int> counter;
    for (int num : nums) {
        counter[num]++;
    }

    for (auto& it : counter) {
        int key = it.first;
        int value = it.second;
        cout << key << " " << value << endl;
    }

    unordered_set<int> visited;
    unordered_set<string> visited2;

    visited.insert(1);
    visited.insert(2);

    visited.size();
    visited.count(1); // 존재 여부
    visited.empty();

    queue<int> q;
    queue<string> q2;

    q.push(1);
    q.push(2);
    q.front();
    q.pop();

    stack<int> stk;
    stack<string> stk2;

    stk.size();
    stk.push(1);
    stk.push(2);
    stk.top();
    stk.pop();

    

    cout << "Helloworld" << endl;
    return 0;
}