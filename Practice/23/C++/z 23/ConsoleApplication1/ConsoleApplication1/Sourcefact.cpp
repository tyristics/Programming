#include "Headerfact.h"

int Fact(int i)
{
	int n = 1;
	for (i; i > 0; i--) {
		n = n * i;
	}
	return n;
}