import offerhelper
from offerhelper import ListNode


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        mHead = head
        if self.getSize(mHead) < k:
            return None
        
        fast = slow = head
        for i in range(k):
            fast = fast.next
            
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
        
    def getSize(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size


def test(solution):
    testcases = (
            ([], 0, None),
            ([], -1, None),
            ([1, 2, 3], 4, None),
            ([1, 2, 3], 2, 2),
            )

    for testcase in testcases:
        head = offerhelper.create_linked_list(testcase[0])
        k = testcase[1]
        expected = testcase[2]

        ret = solution.FindKthToTail(head, k)
        if not ret:
            assert ret == expected,\
                   f"{testcase} failed: "\
                   f"{ret} != {expected}"
        else:
            assert ret.val == expected,\
                   f"{testcase} failed: "\
                   f"{ret} != {expected}"


def bench_mark():
    solution = Solution()

    test(solution)

if __name__ == '__main__':
    bench_mark()

