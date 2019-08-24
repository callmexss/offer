#include <iostream>

using namespace std;

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
    C(int a, int b, int c) : B1(a), c1(b), j(c) { cout << "*3" << endl; }
    ~C(){ cout << "#3" << endl; }
private:
    B1 c1;
    B2 c2;
};

int main(int argc, const char *argv[])
{
    C c(1, 2, 3);
    return 0;
}
