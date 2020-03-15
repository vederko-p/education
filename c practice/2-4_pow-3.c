#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, t;

    t = scanf("%d", &n);
    if (t != 1)
        return 1;

    while(n > 1) {
        if (n % 3 == 0)
            n /= 3;
        else
            return print("no");
    }
    return print("yes");

    return 0;
}
