#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	double a;
	double x;
	x = 1;
	int b;
	cin >> a;
	cin >> b;
	while (b != 0) {
		x = x * a;
		b = b - 1;
	}
	cout << x;
}