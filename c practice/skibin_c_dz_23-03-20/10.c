#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>


int count_digits(char *s){
    int t=0, i=0;
    while(s[i] != '\0'){
        if(isdigit(s[i]))
            t++;
        i++;
    }

    return t;
}


int main()
{
    char str[10];

    scanf("%9s", str);
    printf("string: %s\n", str);

    int x;
    x = count_digits(str);
    printf("number of digits: %d\n", x);

    return 0;
}
