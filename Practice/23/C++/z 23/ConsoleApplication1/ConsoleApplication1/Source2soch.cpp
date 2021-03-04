#include "Header2soch.h"
#include "Headerfact.h"

int s(int k, int n)
{
	int c = 0;
	c = Fact(n) / (Fact(k) * Fact(n - k));
	return c;
}