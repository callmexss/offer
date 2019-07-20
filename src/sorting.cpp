#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <ctime>

#include <sorttesthelper.h>

using namespace std;


template <typename T>
void insertionSort(std::vector<T> &vec, int l, int r)
{
    // insertion sort vec[l..r]
    for (int i = l+1; i <= r; ++i)
    {
        T e = vec[i];
        int j = i;
        // find a right location for e
        for (; j > l && e < vec[j-1]; j--)
        {
            vec[j] = vec[j - 1];
        }
        vec[j] = e;
    }
}

template <typename T>
void __merge(vector<T> &vec, int l, int mid, int r)
{
    // vec[l..r]
    // vector(l, r) -> [l,r)
    // so r + 1
    vector<T> tmp(&vec[l], &vec[r+1]);
    int i = l; // merge vec[l..mid]
    int j = mid+1; // merge vec[mid+1..r]
    int k = l;

    while (i <= mid || j <= r)
    {
        if (i > mid)
        {
            vec[k++] = tmp[j - l];
            j++;
        }
        else if (j > r)
        {
            vec[k++] = tmp[i - l];
            i++;
        }
        else if (vec[i] <= vec[j])
        {
            vec[k++] = tmp[i - l];
            i++;
        }
        else
        {
            vec[k++] = tmp[j - l];
            j++;
        }
    }
}

template <typename T>
void __mergeSort(vector<T> &vec, int l, int r)
{
    // vec[l..r]
    if (l >= r)
        return;
    int mid = l + ((r - l) >> 2);
    __mergeSort(vec, l, mid);
    __mergeSort(vec, mid+1, r);
    __merge(vec, l, mid, r);
}

template <typename T>
void mergeSort(vector<T> &vec)
{
    __mergeSort(vec, 0, vec.size() - 1);
}

template <typename T>
int __partition(std::vector<T> &vec, int l, int r)
{
    // vec[l..r]
//    int loc = l + (rand() % (r - l + 1));
//    swap(vec[r], vec[loc]);
    T pivot = vec[r];
    int i = l;

    for (int k = l; k <= r; ++k)
        cout << vec[k] << " ";
    cout << endl;

    for (int j = l; j <= r-1; ++j)
    {
        if (vec[j] < pivot)
        {
            swap(vec[i], vec[j]);
            i++;
        }
    }
    swap(vec[i], vec[r]);

    for (int k = l; k <= r; ++k)
        cout << vec[k] << " ";
    cout << endl;

    cout << i << endl;
    cout << "----------------------------" << endl;
    return i;
}

template <typename T>
void __quikcSort(std::vector<T> &vec, int l, int r)
{
    if (l >= r)
        return ;

    int p = __partition(vec, l, r);
    __quikcSort(vec, l, p - 1);
    __quikcSort(vec, p + 1, r);
}

template <typename T>
void quickSort(std::vector<T> &vec)
{
    srand(time(NULL));
    __quikcSort(vec, 0, vec.size() - 1);
}

int main(int argc, const char *argv[])
{
    vector<int> vec{1, 3, 4, 2, 5, 7, 9};
    mergeSort(vec);
    assert(is_sorted(vec.begin(), vec.end()) == true);

    //for (int i : vec)
    //{
    //    cout << i << " ";
    //}
    //cout << endl;

    vector<int> vec1{1, 3, 4, 2, 5, 7, 9};
    // vector<int> vec1{1, 3, 4, 2};
    quickSort(vec1);
    for (int i : vec1)
        cout << i << " ";
    cout << endl;
    assert(is_sorted(vec1.begin(), vec1.end()) == true);

    SortTestHelper::printVector(vec1);

    vector<int> vec2{1, 3, 4, 2, 5, 7, 9};
    insertionSort(vec2, 2, 5);
    assert(is_sorted(vec2.begin()+2, vec2.begin()+6));
    SortTestHelper::printVector(vec2);

    return 0;
}
