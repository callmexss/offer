#include <iostream>
#include <vector>

#include <sorttesthelper.h>

using namespace std;


template <typename T>
int binarySearch(std::vector<T> vec, T target)
{
    int l = 0;
    int r = vec.size() - 1;
    // vec[l..r] still needs to be checked.
    while (l <= r)
    {
        int mid = l + ((r - l) >> 1);
        if (vec[mid] == target)
            return mid;
        else if (vec[mid] > target) // vec[l..mid-1]
        {
            r = mid - 1;
        }
        else // vec[mid+1..r]
        {
            l = mid + 1;
        }
    }
    return -1;
}

template <typename T>
int __binarySearchRecursion(std::vector<T> &vec, T target, int l, int r)
{
    // cout << l << " " << r << endl;
    if (l > r)
        return -1;

    int mid = l + ((r - l) >> 1);
    if (vec[mid] == target)
    {
        return mid;
    }
    if (vec[mid] > target) // vec[l..mid-1]
    {
        return __binarySearchRecursion(vec, target, l, mid - 1);
    }
    else
    {
        return __binarySearchRecursion(vec, target, mid + 1, r);
    }
}

template <typename T>
int binarySearchRecursion(std::vector<T> &vec, T target)
{
    return __binarySearchRecursion(vec, target, 0, vec.size() - 1);
}

int main(int argc, const char *argv[])
{
    std::vector<int> vec = SortTestHelper::generateNearlyOrderedIntVector(100, 0);
    SortTestHelper::printVector(vec);
    assert(binarySearch(vec, 0) == binarySearchRecursion(vec, 0));
    assert(binarySearch(vec, 10) == binarySearchRecursion(vec, 10));
    assert(binarySearch(vec, 50) == binarySearchRecursion(vec, 50));
    assert(binarySearch(vec, 150) == binarySearchRecursion(vec, 150));
    
    return 0;
}
