#include <iostream>
using namespace std;

int main()
{
    int T;
    int num1, num2;
    cin >> T;
    int * answer = new int[T];

    for(int i = 0; i < T; i++){
        cin >> num1 >> num2;
        answer[i] = num1 + num2;
    } 
    
    for(int i = 0; i < T; i++){
        cout << answer[i] << endl;
    } 

    delete[] answer;
    return 0;
}

