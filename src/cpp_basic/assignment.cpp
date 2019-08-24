#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int x = 6;
    x += x -= x * x;
    std::cout << x << std::endl;
    return 0;
}
