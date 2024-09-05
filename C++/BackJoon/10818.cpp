#include <iostream>
using namespace std;

int main()
{
	int COUNT = 0;
	cin >> COUNT;
	int * numList = new int[COUNT];

	for(int i = 0; i < COUNT; i++)
	{
		cin >> numList[i];
	}

	int min = 1000000, max = -1000000;
	for(int i = 0; i < COUNT; i++)
	{
		if(numList[i] < min){
			min = numList[i];
		}
		if(numList[i] > max)
		{
			max = numList[i];
		}
	}

	cout << min << " " << max << "\n";
	return 0;
}