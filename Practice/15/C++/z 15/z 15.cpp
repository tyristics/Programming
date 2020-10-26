#include <iostream>
#include <random>
using namespace std;
int main()
{   
    int qw, z, n, x;
    qw = 1;
    while (qw == 1) {
        n = rand() % 101;
        cout << "Приветственное сообщение от игры";
        cin >> n;
        z = 4;
        while (z > 0) {
            if (x < n) {
                cout << "Загаданное число больше";
                cin >> n;
                z -= 1;
            }
            if (x > n) {
                cout << "Загаданное число меньше";
                cin >> n;
                z -= 1;
            }
            if (x < n) {
                cout << "Загаданное число больше";
                cin >> n;
                z -= 1;
            }
            if (x == n) {
                cout << "Поздравляю! Вы угадали";
            }
        }
        cout << "Вы проиграли. Было загадано:" << n << endl << "Хотите начать сначала? (1 - ДА )";
        cin >> qw;
    }
}

