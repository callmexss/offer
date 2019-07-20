"""
File: 25_merge.py
Author: callmexss
Email: callmexss@126.com
Github: https://github.com/callmexss
Description: 
"""
import offerhelper
from offerhelper import ListNode


class Solution:
    def Merge(self, pHead1, pHead2):
        head = ListNode(0)
        cur = head

        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                cur = cur.next
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                cur = cur.next
                pHead2 = pHead2.next

        cur.next = pHead1 if pHead1 else pHead2
        return head.next


# TODO: recursion solution
class Solution:
    def Merge(self, pHead1, pHead2):
        pass


def test(solution):
    testcases = (
            ([], [], []),
            ([1], [1], [1, 1]),
            ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
            ([1, 2, 3], [2, 2, 3], [1, 2, 2, 2, 3, 3]),
            )

    for testcase in testcases:
        pHead1 = offerhelper.create_linked_list(testcase[0])
        pHead2 = offerhelper.create_linked_list(testcase[1])
        ret = solution.Merge(pHead1, pHead2)
        merged = offerhelper.convert_linked_list_to_list(ret)

        assert merged == testcase[-1],\
               f"{testcase} failed: "\
               f"{merged} != {testcase[-1]}"


def bench_mark():
    solution = Solution()

    test(solution)
    print("All testcase passed")


if __name__ == '__main__':
    bench_mark()

