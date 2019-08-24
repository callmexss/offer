#include <stdio.h>

#define N 20

void fun(int a[], int n, int m)
{  
    int i, j;
    for(i=m; i>=n; i--)
        a[i+1] = a[i];
}

int main()
{
    int i, a[N] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    fun(a, 2, 9);
    for(i=0; i<5; i++)
        printf("%d", a[i]);
    return 0;
}
