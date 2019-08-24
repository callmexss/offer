#include<stdio.h>
#include<inttypes.h>

int main()
{
    uint32_t a = 100;
    while (a > 0)
    {
        --a;
    }
    printf("%d", a);
    return 0;
}
