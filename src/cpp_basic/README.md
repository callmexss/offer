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

无符号整数可以取到 0，最后一次循环 `a = 1; --a;` 后判断 `0 > 0` 为假，退出循环。如果循环条件为 `a >= 0` 则死循环。
