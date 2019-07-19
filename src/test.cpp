#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;

class A
{
public:
    void f1() { }
    virtual void f2() {}
};


int main(int argc, const char *argv[])
{
    int *b = (int*) malloc (10);
    if (b == nullptr)
        cout << "allocated failed" << endl;
    std::cout << sizeof(b) << std::endl;
    free(b);

//    A* a = nullptr;
//    a->f1();
//    a->f2();

    std::vector<int> v{1, 2, 3, 4, 5};
    std::vector<int> v1{&v[1], &v[3]};
    for (int i : v1)
        cout << i << " ";
    cout << endl;

    return 0;
}
