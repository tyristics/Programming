#include <iostream>

using namespace std;
int main()
{
	int a;
	cin >> a;
	if ((a % 2 != 0) and (a % 3 != 0) and (a % 5 != 0) and (a % 7 != 0)) {
		cout << "Простое";
	}
	if((a % 2 == 0) and (a % 3 == 0) and (a % 5 == 0) and (a % 7 == 0)) { 
		cout << "Составное"; 
	}
}