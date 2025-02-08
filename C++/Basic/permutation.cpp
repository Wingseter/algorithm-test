#include <iostream>
#include <vector>

using namespace std;

void permutation(vector<int>& nums, vector<bool>& visited, vector<int>& current){
    if (current.size() == nums.size()){
        for (int i = 0; i < current.size(); i++){
            cout << current[i] << " ";
        }
        cout << endl;
        return;
    }

    for (int i = 0; i < nums.size(); i++) {
        if (!visited[i]){
            visited[i] = true;
            current.push_back(nums[i]);
            permutation(nums, visited, current);
            current.pop_back();
            visited[i] = false;
        }
    }

}

int main(){
    vector<int> nums = {1, 2, 3};
    vector<bool> visited(nums.size(), false);
    vector<int> current;
    permutation(nums, visited, current);

}