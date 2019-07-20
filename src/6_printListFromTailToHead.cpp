#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>
#include <tuple>
#include <memory>

#include "offerhelper.h"

using namespace std;

class BaseSolution
{
public:
    virtual std::vector<int> printListFromTailToHead(ListNode* head) = 0;
};


/**
 * Simple use a stack.
 */
class Solution: public virtual BaseSolution
{
public:
    vector<int> printListFromTailToHead(ListNode* head) override
    {
        std::vector<int> vec;
        while (head)
        {
            vec.push_back(head->val);
            head = head->next;
        }
        reverse(vec.begin(), vec.end());
        return vec;
    }
};


/**
 * Insert at the begining.
 */
class Solution1: public virtual BaseSolution
{
public:
    vector<int> printListFromTailToHead(ListNode* head) override
    {
        // insertion
        ListNode *newHead = new ListNode(0);
        while (head)
        {
            ListNode *saved_next = head->next;
            head->next = newHead->next;
            newHead->next = head;
            head = saved_next;
        }

        std::vector<int> vec;
        head = newHead->next;
        while (head)
        {
            vec.push_back(head->val);
            head = head->next;
        }
        return vec;
    }
};

/**
 * Recursion soluton.
 */
class Solution2: public virtual BaseSolution
{
public:
    vector<int> printListFromTailToHead(ListNode* head) override
    {
        std::vector<int> vec;
        if (head)
        {
            auto ret = printListFromTailToHead(head->next);
            vec.insert(vec.end(), ret.begin(), ret.end());
            vec.push_back(head->val);
        }
        return vec;
    }
};

/**
 * Use either move semantic or reference will be fine.
 */
void test(unique_ptr<BaseSolution> pSolution)
{
    int n = 10000;
    std::vector<int> largeRandomVector = Offer::genRandomVector(n, 0, n);
    std::vector<vector<int>> testCases{
        {},
        {1},
        {1, 2, 3},
        largeRandomVector,
    };

    for (auto v : testCases)
    {
        // cout << "testcase: ";
        // Offer::printVec(v);
        ListNode* head = Offer::createLinkedList(v);
        auto ret = pSolution->printListFromTailToHead(head);
        reverse(v.begin(), v.end());
        assert(ret == v);
    }

    cout << "All testcases passed" << endl;

}

void benchMark()
{
    unique_ptr<BaseSolution> pSolution = make_unique<Solution>();
    unique_ptr<BaseSolution> pSolution1 = make_unique<Solution1>();
    unique_ptr<BaseSolution> pSolution2 = make_unique<Solution2>();

    test(move(pSolution));
    test(move(pSolution1));
    test(move(pSolution2));
}


int main(int argc, char **argv)
{
    benchMark();
    
    return 0;
}
