#include <iostream>
#include <string>
using namespace std;
int main()
{
    setlocale(LC_ALL, "Russian");
    double a;
    double c;
    string b;
    double z;
    cin >> a;
    cin >> b;
    cin >> c;
    if (b == "*") {
        z = a * c;
        cout << z;
    }
    if (b == "-") {
        z = a - c;
        cout << z;
    }
    if (b == "+") {
        z = a + c;
        cout << z;
    }
    if (b == "/") {
        z = a / c;
        cout << z;
    }
}