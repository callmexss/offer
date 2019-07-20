#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

#include "offerhelper.h"

using namespace std;

int main(int argc, const char *argv[])
{
    std::vector<int> vec{1, 2, 3, 4, 5};
    ListNode *head = Offer::createLinkedList(vec);
    Offer::printLinkedList(head);
    auto randomVec = Offer::genRandomVector();
    Offer::printVec(randomVec);
    
    return 0;
}
