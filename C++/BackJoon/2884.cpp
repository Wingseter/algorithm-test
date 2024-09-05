#include <iostream>
#define MAX_HOUR 24
#define MAX_MINUTE 60
using namespace std;

int main()
{
    int hour, minute;

    // 숫자 입력
    cin >> hour >> minute;
    
    if (minute - 45 < 0)
    {
        if(hour - 1 < 0){
            cout << MAX_HOUR - 1 << ' ' << MAX_MINUTE + minute - 45 << endl;
        }
        else {
            cout << hour - 1 << ' ' << MAX_MINUTE + minute - 45 << endl;
        }
    }
    else if (minute - 45 >= 0)
    {
        cout << hour << ' ' << minute - 45 << endl;
    }
    
    return 0;
}

