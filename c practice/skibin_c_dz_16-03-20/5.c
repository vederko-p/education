#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, k=1;

    int t;
    t = scanf("%d", &n);
    if(t != 1)
        return 1;

    while(pow(k, 3) <= n)
        k++;

    if(k*k*k == n)
        printf("%d", k);
    else
        printf("%d", 0);

    return 0;
}
