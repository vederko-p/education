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


int plus_str(char *s1, char *s2){

    char *k;
    int l1 = len(s1);
    int l2 = len(s2);
    k = malloc((l1 + l2)*sizeof(char));

    int i = 0;
    for(i = 0; i < l1; i++)
        k[i] = s1[i];
    for(i = l1; i < l1 + l2; i++)
        k[i] = s2[i-l1];
    k[l1+l2] = '\0';

    return k;
}


int main()
{
    char str1[10], str2[10];

    scanf("%9s %9s", str1, str2);
    printf("strings:\n%s\n%s\n", str1, str2);

    printf("union string: %s\n", plus_str(str1, str2));

    return 0;
}
