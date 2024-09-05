#include <iostream>
using namespace std;

int main()
{
    int T;

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> T;
    int * num1 = new int[T];
    int * num2 = new int[T];

    for(int i = 0; i < T; i++){
        cin >> num1[i] >> num2[i];
    }

    for(int i = 0; i < T; i++){
        cout << "Case #" << i + 1 << ": "\
            << num1[i] << " + " << num2[i] << " = "\
            << num1[i] + num2[i] << '\n';
    }

    delete[] num1;
    delete[] num2;
    return 0;
}

