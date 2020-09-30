#include <iostream>
#include <math.h>
using namespace std;
int main()
{
    setlocale(LC_ALL, "Russian");
    double a;
    cin >> a;
    double b;
    cin >> b;
    double c;
    cin >> c;
    double x, x1, x2, d, xsqrt;
    if ((a == 0) && (b != 0) && (c != 0)) {
        x = (-c) / b;
        cout << "x = " << x;
    }
    if ((a == 0) && (b == 0) && (c != 0)) {
        cout << "Нет решений";
    }
    if ((a == 0) && (b != 0) && (c == 0)) {
        cout << "x = " << 0;
    }
    if ((a == 0) && (b == 0) && (c == 0)) {
        cout << "Нет решений";
    }
    if ((a != 0) && (b == 0) && (c != 0)) {
        xsqrt = (-c) / a;
        if (xsqrt < 0) {
            cout << "Нет решений";
        }
        if (xsqrt == 0) {
            cout << "x = " << 0;
        }
        else {
            x1 = -sqrt(xsqrt);
            x2 = sqrt(xsqrt);
            cout << "x1 = " << x1 << endl << "x2 = " << x2;
        }
    }
    if ((a != 0) && (b != 0) && (c == 0)) {
        x = (-b) / a;
        cout << "x1 = " << 0 << endl << "x2 = " << x;
    }
    if ((a != 0) && (b == 0) && (c == 0)) {
        cout << "Нет решений";
    }
    if ((a != 0) && (b != 0) && (c != 0)){
        d = b * b - 4 * a * c;
        if (d == 0) {
            x = (-b) / 2 * a;
            cout << "x = " << x;
        }
        if (d > 0) {
            x1 = ((-b) + sqrt(d)) / 2 * a;
            x2 = ((-b) - sqrt(d)) / 2 * a;
            cout << "x1 = " << x1 << endl << "x2 = " << x2;
        }
        else {
            cout << "Нет решений" ;
        }
    }
}