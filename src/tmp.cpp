#include <iostream>
#include "tmp.h"

using namespace std;


int main(int argc, const char *argv[])
{
    auto ret = staticFunc();
    std::cout << ret << std::endl;

    char str[] = "hello";
    char *p = str;
    p++;
    cout << str << endl;
    cout << p << endl;
    
    return 0;
}
