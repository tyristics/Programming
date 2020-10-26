#include <iostream>

using namespace std;
int main()
{
	long long a;
    int z;
	cin >> a;
    z = 0;
    while (a != 1){
        if (a % 2 == 0) {
            a = a / 2;
            z += 1;
        }
        else {
            a = a - 1;
        }
	}
    cout << z;
}