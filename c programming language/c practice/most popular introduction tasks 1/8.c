#include <stdio.h>
#include <stdlib.h>


int main()
{
    int n, k=1;

    int h;
    h = scanf("%d", &n);
    if(h != 1)
        return 0;

    int l=0, t=n;

    while(t != 0){
        l++;
        t /= 10;
    }

    int N=l, a[N];
    int i;

    for(i = 0; i < N; i++){
        a[i] = n % 10;
        n /= 10;
    }

    for(i = 0; i <= N/2; i++){
        if(a[N-1-i] != a[i])
            k = 0;
            break;
    }

    printf("%d", k);

    return 0;
}
