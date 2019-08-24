#include <iostream>
using namespace std;

class A
{
public:
    void f() { std::cout << "A" << std::endl; }
};

class B : public A
{
public:
    virtual void f() { std::cout << "B" << std::endl; }
};

int main(int argc, char **argv)
{
    A* a = new B();
    a->f();
    delete a;
    
    return 0;
}
