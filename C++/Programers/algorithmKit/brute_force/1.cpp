#include <vector>
#include <climits>

using namespace std;

int bruteforce(vector<vector<int>>& sizes) {
    int min_area = 0;
    int min_x = 0, min_y = 0;
    
    for(auto size : sizes) {
        int w = size[0];
        int h = size[1];
        
        if(w > h) {
            swap(w, h);
        }
        
        min_x = max(min_x, w);
        min_y = max(min_y, h);
    }
    
    min_area = min_x * min_y;

    return min_area;
}

int solution(vector<vector<int>> sizes) {
    return bruteforce(sizes);
}
