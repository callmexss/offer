# CPP 牛客笔记本

## 基础数据类型

### 整形

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
