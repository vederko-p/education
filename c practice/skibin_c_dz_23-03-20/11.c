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


char * double_str(char *s){

    char *k;
    int l = len(s);
    k = malloc((2*l+1)*sizeof(char));

    int i = 0;
    for(i = 0; i < l; i++){
        k[i] = k[l + i] = s[i];
    }
    k[2*l] = '\0';

    return k;
}


int main()
{
    char str[10];

    scanf("%9s", str);
    printf("string: %s\n", str);

    printf("double string: %s\n", double_str(str));

    return 0;
}
