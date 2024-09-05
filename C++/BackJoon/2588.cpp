#include <iostream>
using namespace std;

int main()
{
    int a, b;
    int temp;

    // a, b 입력
    cin >> a;
    cin >> b;
    
    temp = b;
    while(temp != 0){
        cout << a * (temp % 10) << endl;
        temp = temp / 10;
    }
    cout << a * b << endl;

    return 0;
}

