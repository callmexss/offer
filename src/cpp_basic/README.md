# CPP 牛客笔记本

## 基础数据类型

### 整型

1. [以下代码运行结果为（）](./uint32_t1.cpp)

```cpp
#include<stdio.h>
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
```

无符号整数可以取到 0，最后一次循环 `a = 1; --a;` 后判断 `0 > 0` 为假，退出循环。如果循环条件为 `a >= 0` 则死循环，因为当 `a = 0` 时，`0 >= 0` 还可以进入循环体，此时 `--a;` 会溢出，结果是 `uint32_t` 所能表示的最大值。


2. [以下代码的输出为 24 的说法是否正确？](./assignment.cpp)

```cpp
#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int x = 6;
    x += x -= x * x;
    std::cout << x << std::endl;
    return 0;
}
```

从👉向👈：

    1. x -= x * x; -> x = 6 - 6 * 6 = -30

    2. x += x; -> x = -30 + (-30) = -60


### 数组

1. [以下程序的输出结果是（ ）。](./array.cpp)

A. 31

B. 13

C. 10

D. 20

```cpp
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
```

从第 3 个元素开始，后一个元素被前一个元素覆盖。{1, 2, 3, 3, 4, 5, ...}
