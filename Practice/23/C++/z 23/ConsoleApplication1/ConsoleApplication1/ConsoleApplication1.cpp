#include <iostream>
#include "Headerfact.h"
#include <iomanip>
#include "Header1sin.h"
#include "Header2soch.h"
#define cout std::cout


int main()
{
    cout << "n" << "\t" << "n!\n";
    for (int n = 0; n <= 10; n++) {
        cout << n << "\t" << Fact(n) << "\n";
    }
    cout << "\n";

    float pi = 3.14;
    for (float x = 0; x <= pi / 4; x = x + pi / 180)
    {
        cout << x << "\t" << std::setprecision(4) << Sin(x) << "\n";
    }
    cout << "\n";

    cout << "k" << "\t" << "c(k, 10)\n";

    for (int k = 1; k <= 10; k++)
    {
        cout << k << "\t" << s(k, 10) << "\n";
    }
}