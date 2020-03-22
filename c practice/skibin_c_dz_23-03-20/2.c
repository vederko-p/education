#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 10


int main()
{

    int a[N];
    double r, m;

    int t;
    t = scanf("%lf", &r);
    if(t != 1)
        return 1;

    srand(time(NULL));

    int i;
    for(i = 0; i < N; i++)
        a[i] = rand()%100;

    printf("mass a:\n");
    for(i = 0; i < N; i++)
        printf("%d\n", a[i]);

    int r1;
    m = abs(r - (double) a[0]);
    r1 = a[0];
    for(i = 1; i < N; i++){
        if(abs((double) a[i] - r) < m){
            r1 = a[i];
            m = abs(r - (double) a[i]);
        }
    }

    printf("closest to %f is: %d", r, r1);

    return 0;
}
