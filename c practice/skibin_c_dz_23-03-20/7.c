#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 10


int main()
{

    int a[N];

    int i;
    for(i = 0; i < N/2; i++)
        a[i] = i+1;
    for(i = N/2; i < N; i++)
        a[i] = 10 - i;

    /* a[3] = 100; */

    printf("mass a:\n");
    for(i = 0; i < N; i++)
        printf("%d\n", a[i]);

    for(i = 0; i <= N/2; i++){
        if(a[N-1-i] != a[i]){
            printf("no");
            return 0;
        }
    }

    printf("yes");

    return 0;
}
