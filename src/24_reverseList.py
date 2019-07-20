import offerhelper
from offerhelper import ListNode


class Solution:
    def ReverseList(self, pHead):
        mHead = ListNode(0)
        pre = mHead
        cur = pHead
        while cur:
            saved_next = cur.next
            cur.next = pre.next 
            pre.next = cur
            cur = saved_next
        return mHead.next
        

# TODO: recursion solution
class Solution2:
    def ReverseList(self, pHead):
        pass


def test(solution):
    testcases = (
            ([], []),
            ([1], [1]),
            ([1, 2, 3], [3, 2, 1]),
            )

    for testcase in testcases:
        head = offerhelper.create_linked_list(testcase[0])
        newHead = solution.ReverseList(head)
        ret = offerhelper.convert_linked_list_to_list(newHead)
        assert ret == testcase[1],\
               f"{testcase} failed: "\
               f"{ret} != {testcase[1]}"

def bench_mark():
    solution = Solution()

    test(solution)

if __name__ == '__main__':
    bench_mark()

