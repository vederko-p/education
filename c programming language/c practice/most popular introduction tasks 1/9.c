#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main()
{
    int n, s=0, f=1;

    int t;
    t = scanf("%d", &n);
    if(t != 1)
        return 1;

    while(n != 0){
        if(n % 10 - 2 > 0){
            s += n%10 * f;
            f *= 10;
        }
        n = n / 10;
    }

    printf("%d\n", s);

    return 0;
}
