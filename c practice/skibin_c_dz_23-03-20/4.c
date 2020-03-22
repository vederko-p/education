#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 10


int main()
{

    int a[N];

    int i;
    for(i = 0; i < 2; i++)
        a[i] = 1;
    for(i = 2; i < 7; i++)
        a[i] = 2;
    for(i = 6; i < N; i++)
        a[i] = 3;

    printf("mass a:\n");
    for(i = 0; i < N; i++)
        printf("%d\n", a[i]);

    for(i = 0; i < N-1; i++){
        if(a[i] > a[i+1]){
            printf("sorted?: %d", 0);
            return 0;
        }
    }

    printf("sorted?: %d", 1);

    return 0;
}
