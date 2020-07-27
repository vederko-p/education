#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 10


int main()
{

    int a[N];

    int i;
    for(i = 0; i < 2; i++)
        a[i] = 3;
    for(i = 2; i < 7; i++)
        a[i] = 1;
    for(i = 6; i < N; i++)
        a[i] = 0;

    printf("mass a:\n");
    for(i = 0; i < N; i++)
        printf("%d\n", a[i]);

    int s=0;
    int si = 0;
    int j = 0;
    for(i = 0; i < N; i++){
        for(j = 0; j< N; j++){
            if(a[i] == a[j])
                si++;
        }
        if(si > s)
            s = si;
        si = 0;
    }

    printf("max number of duplicates: %d\n", s);

    return 0;
}

