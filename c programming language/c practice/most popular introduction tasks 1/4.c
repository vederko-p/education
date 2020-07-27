#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, k=1;

    int t;
    t = scanf("%d", &n);
    if(t != 1)
        return 1;

    while(pow(k, 2) <= n)
        k++;

    printf("%d", k);

    return 0;
}
