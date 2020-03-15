#include <stdio.h>
#include <stdlib.h>

int fact(int n)
{
    if(n != 1)
        return n * fact(n-1);
    else
        return n;
}

int main()
{
    int n, k, q = 1;
    double s = 1.0;

    n = scanf("%d", &k);
    if (n != 1)
        return 1;

    while(q != k) {
        s += (double) 1 / fact(q);
        q++;
    }

    printf("%f\n", s);

	return 0;
}
