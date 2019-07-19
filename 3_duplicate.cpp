#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;


bool duplicate(int numbers[], int length, int* duplication)
{
    if (length <= 0)
        return false;
    
    for (int i = 0; i < length; ++i)
    {
        while (numbers[i] != i)
        {
            if (numbers[i] == numbers[numbers[i]])
            {
                *duplication = numbers[i];
                return true;
            }
            swap(numbers[i], numbers[numbers[i]]);
        }
    }
    return false;
}

int main(int argc, char **argv)
{
    
    return 0;
}

