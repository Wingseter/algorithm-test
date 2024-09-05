#include <iostream>
using namespace std;

int main()
{
    int a;

    // 숫자 입력
    cin >> a;
    
    cout << (a % 4 == 0 && a % 100 != 0 || a % 400 == 0) << endl;
    return 0;
}

