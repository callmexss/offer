#include <iostream>
using namespace std;

int cnt = 0;

int x(int n)
{
    cnt++;
    if (n<=3)
    {
        return 1;
    }
    else
    {
        return x(n-2)+x(n-4)+1;
    }
}

int main(int argc, const char *argv[])
{
    x(x(8));
    std::cout << cnt << std::endl;
    return 0;
}
