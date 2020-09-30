#include <iostream>
using namespace std;
int main()
{
    setlocale(LC_ALL, "Russian");
    int a;
    int b;
    int c;
    cout << "Введите а = ";
    cin >> a;
    cout << "Введите b = ";
    cin >> b;
    c = b;
    b = a;
    a = c;
    cout << "a = ";
    cout << a;
    cout << endl << "b = ";
    cout << b << endl;
}



