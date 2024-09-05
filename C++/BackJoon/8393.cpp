#include <iostream>
using namespace std;

int main()
{
    int num1;
    cin >> num1;

    int sum = 0;
    for(int i = 1; i <= num1; i++){
        sum += i;
    } 
    
    cout << sum << endl;
    return 0;
}

