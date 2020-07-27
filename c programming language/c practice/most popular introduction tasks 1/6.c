#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, k;
    int min, max;

    int t;
    t = scanf("%d %d", &a, &b);
    if(t != 2)
        return 1;

    if(a > b)
        max = a;
    else
        max = b;

    if(a > b)
        min = b;
    else
        min = a;

    k = max;
    while(k % min != 0){
        k += max;
    }

    printf("%d", k);

    return 0;
}
