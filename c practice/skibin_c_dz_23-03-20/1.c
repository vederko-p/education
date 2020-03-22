#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 10


int main()
{

    int a[N];

    srand(time(NULL));

    int i;
    for(i = 0; i < N; i++)
        a[i] = rand()%100;

    printf("mass a start:\n");
    for(i = 0; i < N; i++)
        printf("%d\n", a[i]);

    int imin, imax;
    imin = imax = 0;
    for(i = 0; i < N; i++){
        if(a[imin] > a[i])
            imin = i;
        if(a[imax] < a[i])
            imax = i;
    }

    int t;
    t = a[imin];
    a[imin] = a[imax];
    a[imax] = t;

    printf("mass a end:\n");
    for(i = 0; i < N; i++)
        printf("%d\n", a[i]);

    return 0;
}
