#include "Header.h"

#include "Header.h"

int otw(int a)
{
    long long b = 1;
    while (a > 1) {
        a = a - 1;
        b = a * b;
    }
    a = b;
    return a;
}

