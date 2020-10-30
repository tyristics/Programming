#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()
{   
    int qw, z, n, x;
    qw = 1;
    while (qw == 1) {
        srand(static_cast<unsigned int>(time(0)));
        int x = rand() % 101 + 0
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

