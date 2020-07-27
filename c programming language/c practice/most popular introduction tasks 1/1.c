#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n = 1, q = 100, s1, s2;

    while(n != q) {
        if (n % 2)
            s1 += n;
        else
            s2 += n;
        n++;
    }

    printf("%d\n%d\n", s1, s2);

    return 0;
}
