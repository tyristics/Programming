#include <iostream>
#include <math.h>
using namespace std;
int main()
{
    setlocale(LC_ALL, "Russian");
    cout << " 1 - ввод параметров треугольника через длины сторон или 2 - ввод параметров через координаты вершин или другое целое число по модулю не более 1000 ";
    double z;
    cin >> z;
    if (z == 1) {
        double a;
        cin >> a;
        double b;
        cin >> b;
        double c;
        cin >> c;
        double s, p;
        p = 0.5 * (a + b + c);
        s = sqrt(p * (p - a) * (p - b) * (p - c));
        cout << "S = " << s;
    }
    if (z == 2) {
        cout << "Введите координаты вершин: три пары вещественных чисел,  каждая пара в отдельной строке, числа в паре разделены пробелом.";
        double x1;
        cin >> x1;
        double y1;
        cin >> y1;
        double x2;
        cin >> x2;
        double y2;
        cin >> y2;
        double x3;
        cin >> x3;
        double y3;
        cin >> y3;
        double s;
        s = 0.5 * (abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)));
        cout  << "S = " << s;
    }
}