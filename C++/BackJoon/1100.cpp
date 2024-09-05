#include <iostream>
using namespace std;

int main()
{

	int orgNum;
	int result;
	int next;
    int COUNT = 0;

	cin >> orgNum;
	next = orgNum;
	do{
		result = next % 10 + next / 10;
		next = next % 10 * 10 + result % 10;
		COUNT++;
	}
	while(next != orgNum);

	cout << COUNT << "\n";
	return 0;
}