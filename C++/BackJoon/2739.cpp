#include <iostream>
#define MAX_HOUR 24
#define MAX_MINUTE 60
using namespace std;

int main()
{
    int num;

    // 숫자 입력
    cin >> num;
    
   for(int i = 1; i < 10; i++)
   {
       cout << num << " * " << i << " = " << num * i << endl;
   }
    
    return 0;
}

