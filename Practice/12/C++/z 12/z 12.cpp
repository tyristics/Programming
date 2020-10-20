#include <iostream>

using namespace std;
int main()
{
	int a;
	long long int x;
	x = 1;
	int b;
	cin >> a;
	b = a;
	while (b != 0) {
		x = x * b;
		b = b - 1;
	}
	cout << x;
}