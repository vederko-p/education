#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 10


int main()
{

    int a[N];

    int i;
    for(i = 0; i < N; i++)
        a[i] = i;

    /* a[1] = 2; */

    printf("mass a:\n");
    for(i = 0; i < N; i++)
        printf("%d\n", a[i]);

    if(a[0]%2 == 0){
        for(i = 1; i<N; i++){
            if(a[i]%2 != i%2){
                printf("not");
                return 0;
            }
        }
    }
    else{
        for(i = 1; i<N; i++){
            if(a[i]%2 != (i+1)%2){
                printf("not");
                return 0;
            }
        }
    }

    printf("yes");

    return 0;
}
