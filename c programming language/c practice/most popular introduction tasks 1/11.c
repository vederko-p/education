#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int f(int n){
    int s=0;
    if(n > 2)
        s += f(n-1) + f(n-2);
    else
        s += 1;

    return s;
}


int main()
{
    int s = f(7);

    printf("%d", s);

    return 0;
}
