#include <iostream>
using namespace std;

int main()
{
    int T;

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> T;

    for(int i = 0; i < T; i++){
        for(int j = 0; j < T-i-1; j++){
            cout << ' ';
        }
        for(int j = 0; j <= i; j++){
            cout << '*';
        }
        cout << '\n';
    }

    return 0;
}

