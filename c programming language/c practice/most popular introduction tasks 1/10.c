#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main()
{
    int n, s=0, f=1;
    double x;

    int t;
    t = scanf("%d %lf", &n, &x);
    if(t != 2)
        return 1;

    int i;
    for(i=0; i < n+1; i++){
        s += f;
        f *= x;
    }

    printf("%d\n", s);

    return 0;
}
