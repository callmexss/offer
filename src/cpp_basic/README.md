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


3. 以下哪个选项可以正确描述sizeof(double)？

A. 一个整型表达式

B. 一个双精度型表达式

C. 一个不合法的表达式

D. 一种函数调用

> sizeof 是 C 语言中的一个操作符 (operator)，不是函数调用，简单的说其作用就是返回一个对象或者类型所占的内存字节数由于结果是无符号整数，因此可以把它看作是无符号整型表达式。所以选择 A。


### 字符串

1. [当执行下面的程序时，如果输入ABC，则输出结果是（）](./string.cpp)

```cpp
#include  <stdio.h> 
#include  <string.h> 

void main() 
{ 
    char ss[10]="1,2,3,4,5";
    gets (ss);
    strcat (ss,"6789");
    printf ("%s\n",ss);
}
```

> 应该这么来解释：
第一步 ss[10] = "1,2,3,4,5";
第二步 gets() 之后，ss[10] = “A,B,C,\0,5"
第三步 strcat() 之后，ss[10] = "A,B,C,6,7,8,9"
strcat会在遇到第一个\0时开始拼接

### 数组

1. [以下程序的输出结果是（ ）。](./array.cpp)

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

A. 31

B. 13

C. 10

D. 20

从第 3 个元素开始，后一个元素被前一个元素覆盖。{1, 2, 3, 3, 4, 5, ...}

## 面向对象

### 构造函数

1. [有以下类定义](./constructor.cpp)

```cpp
class B1
{
    int b1;
public:
    B1(int i) { b1 = i; cout << b1 << endl; }
    ~B1() { cout<<"#1"; }
};

class B2
{
    int b2;
public:
    B2() { b2 = 0; cout<< "*2" << endl; }
    ~B2() { cout << "#2" << endl; }
};

class C: virtual public B1, public B2
{
    int j;
public:
    C(int a, int b, int c) : B1(a), ____, j(c) { cout << "*3" << endl; }
    ~C(){ cout << "#3" << endl; }
private:
    B1 c1;
    B2 c2;
};
```

请为横线处选择合适的程序将派生类C的构造函数补充完整（）

A. B1(b)

B. c1(b)

C. c2(b)

D. B2(b)

C 中有三个成员变量，整型 j，B1 c1, B2 c2。B1 没有默认构造函数需要初始化，B2 有无参的构造函数，可以不显示初始化。因此：

对于 A 选项，基类 B1 已经在初始化列表 B1(a) 中显示初始化过，不能再初始化。

对于 B 选项，成员变量 c1 需要初始化，其构造函数 B1(int i) 需要一个整型作为参数。

对于 C 选项，c2 对应的类 B2 没有带参数的构造函数，会产生错误。

对于 D 选项，同上。

### 多态

1. [下面这段代码运行时会出现什么问题？](./virtual.cpp)

```cpp
class A
{
public:
    void f()
    {
        printf("A\n");
    }
};
 
class B: public A
{
public:
    virtual void f()
    {
        printf("B\n");
    }
};
 
int main()
{
    A *a = new B;
    a->f();
    delete a;
    return 0;
}
```

A. 没有问题，输出 B

B. 不符合预期的输出 A

C. 程序不正确

D. 以上答案都不正确

因为 A 中的 f 没有声明为虚函数，所以 B 中不会体现多态的特性。输出为 A。

