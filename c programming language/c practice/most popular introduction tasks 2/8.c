#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 10


int main()
{

    int a[N], b[N];

    int i;
    for(i = 0; i < 3; i++)
        a[i] = 3;
    for(i = 3; i < 8; i++)
        a[i] = 8;
    for(i = 8; i < N; i++)
        a[i] = 10;

    for(i = 0; i < N; i++)
        b[i] = i+1;

    printf("mass a:\n");
    for(i = 0; i < N; i++)
        printf("%d\n", a[i]);

    printf("mass b:\n");
    for(i = 0; i < N; i++)
        printf("%d\n", b[i]);

    int s = 0;
    int j;
    int last = a[N-1];
    for(i = 0; i < N; i++){
        if (a[i] == last)
                continue;
        for(j = 0; j < N; j++){
            if(a[i] == b[j]){
                last = a[i];
                s++;
                j = N;
            }
        }
    }

    printf("%d", s);

    return 0;
}
