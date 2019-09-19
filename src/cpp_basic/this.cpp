#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;

class A
{
public:
    // this is a right value, can not get its address
    void play() { std::cout << &this << std::endl; }
};

int main(int argc, char **argv)
{
    
    
    return 0;
}
