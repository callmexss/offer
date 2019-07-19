#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <cassert>
#include <algorithm>

using namespace std;

bool find(int target, std::vector<vector<int> > &array)
{
    if (array.empty())
        return false;

    int i = 0; // row
    int j = array[0].size() - 1; // column

    // the border of the array 
    while (i <= array.size() - 1 && j >= 0)
    {
        if (array[i][j] == target)
        {
            return true;
        }
        else if (array[i][j] > target)
        {
            // column--
            j--;
        }
        else // array[i][j] > target
        {
            // row++
            i++;
        }
    }
    return false;
}

int main(int argc, char **argv)
{
    std::vector<vector<int> > vec{
        {1, 2, 3, 4, 5},
        {2, 3, 4, 5, 6},
        {4, 5, 7, 10, 13},
        {13, 16, 18, 21, 23},
    };

    int target = 7;

    assert(find(target, vec) == true);
    assert(find(21, vec) == true);
    assert(find(-8, vec) == false);

    return 0;
}
