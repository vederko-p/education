#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>


int len(char *s){
    int i=0, l=0;
    while(s[i] != '\0'){
        l++;
        i++;
    }
    return l;
}


int fatoi(char *s){

    int *k;
    int l;

    l = len(s);
    k = malloc(l*sizeof(char));

    int i;
    for(i=0; i < l; i++)
        k[i] = s[i];



    return k;
}


int main()
{
    char str[10];

    scanf("%9s", str);
    printf("string: %s\n", str);

    printf("%d\n", fatoi(str));

    return 0;
}
