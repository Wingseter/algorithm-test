#include <iostream>
#include <vector>

using namespace std;

void combination(vector<int>& nums, int start, int k, vector<int>& current) {
    if (current.size() == k) {
        for (int i = 0; i < current.size(); i++) {
            cout << current[i] << " ";
        }
        cout << endl;
        return;
    }

    for (int i = start; i < nums.size(); i++) {
        current.push_back(nums[i]);
        combination(nums, i + 1, k, current);
        current.pop_back();
    }
}

int main() {
    vector<int> nums = {1, 2, 3, 4}; 
    int k = 2;  
    vector<int> current;
    
    combination(nums, 0, k, current);
}