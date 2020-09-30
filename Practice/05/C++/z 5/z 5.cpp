#include <iostream>
using namespace std;
int main()
{
    setlocale(LC_ALL, "Russian");
    double g;
    g = 9.8;
    double x;
    double v;
    double t;
    double otv;
    cout << "Введите x, v, t = ";
    cin >> x;
    cin >> v;
    cin >> t;
    otv = x + v * t + 1 / 2* g * t * t;
    cout << otv;
}