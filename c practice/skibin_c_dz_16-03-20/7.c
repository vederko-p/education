#include <stdio.h>
#include <stdlib.h>
#define Na 10
#define Nb 3


int aux(int n){

    int b[Nb], a[Na];
    int i;

    for(i = 0; i < Na; i++)
        a[i] = 0;
    for(i = 0; i < Nb; i++)
        b[i] = 0;

    for(i = 0; i < Nb; i++){
        b[i] = n % 10;
        n /= 10;
    }

    for(i = 0; i < Nb; i++)
        a[b[i]] += 1;

    for(i = 0; i < Na; i++)
        if (a[i] > 1)
            return 1;
    return 0;

}


int main()
{

    int x=102, k=14;

    while(x != 987){
        x++;
        if(aux(x))
            k++;
    }

    printf("%d\n", k);
    printf("%d\n", 999-100+1 - k);

    return 0;
}
