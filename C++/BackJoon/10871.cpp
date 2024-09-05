#include <iostream>
using namespace std;

int main()
{
    int T, numCmp;

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> T;
    cin >> numCmp;

    int * numList = new int[T];

    for(int inputCnt = 0; inputCnt < T; inputCnt++){
        cin >> numList[inputCnt];
    }

    for(int printCnt = 0; printCnt < T; printCnt++){
        if(numList[printCnt] < numCmp){
            cout << numList[printCnt] << " ";
        }
    }
    cout << '\n';
    return 0;
}

