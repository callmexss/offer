#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

struct ListNode
{
    int val;
    struct ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};


namespace Offer
{
    std::vector<int> genRandomVector(int n=10, int l=0, int r=10)
    {
        // [l..r]
        srand(time(NULL));
        std::vector<int> vec;
        for (int i = 0; i < n; ++i)
        {
            vec.push_back((l + rand() % (r - l + 1)));
        }
        return vec;
    }

    template<typename T>
    void printVec(std::vector<T> vec)
    {
        for (auto const &v : vec)
            std::cout << v << " ";
        std::cout << std::endl;
    }

    ListNode *createLinkedList(std::vector<int> &vec) 
    {
        ListNode head(0);
        ListNode *cur = &head;
        for (int i : vec)
        {
            ListNode *newNode = new ListNode(i);
            cur->next = newNode;
            cur = cur->next;
        }
        return head.next;
    }

    void printLinkedList(ListNode *head)
    {
        while (head)
        {
            std::cout << head->val << " ";
            head = head->next;
        }
        std::cout << std::endl;
    }
}

