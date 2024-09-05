#include <iostream>
using namespace std;
#define COUNT 9

int main()
{
	int numList[COUNT];

	for(int i = 0; i < COUNT; i++)
	{
		cin >> numList[i];
	}

	int max = 0;
	int index = 0;
	for(int i = 0; i < COUNT; i++)
	{
		if(numList[i] > max)
		{
			max = numList[i];
			index = i + 1;
		}
	}

	cout << max << "\n" << index << "\n";
	return 0;
}