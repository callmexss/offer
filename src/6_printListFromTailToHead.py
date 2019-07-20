import offerhelper
from offerhelper import ListNode

class Solution:
    """Simple use a stack."""
    def printListFromTailToHead(self, listNode):
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        return stack[::-1]


class Solution1:
    """Insert at the begining."""
    def printListFromTailToHead(self, listNode):
        head = ListNode(0)
        while listNode:
            saved_next = listNode.next
            listNode.next = head.next
            head.next = listNode
            listNode = saved_next

        li = []
        listNode = head.next
        while listNode:
            li.append(listNode.val)
            listNode = listNode.next

        return li


class Solution2:
    """Recursion solution."""
    # when size of listNode is larger than 995,
    # maximum recursion error will be raised
    def helper(self, listNode, li):
        if not listNode:
            return
        self.helper(listNode.next, li)
        li.append(listNode.val)

    def printListFromTailToHead(self, listNode):
        li = []
        self.helper(listNode, li)
        return li


class Solution3:
    """Recursion solution."""
    # when size of listNode is larger than 995,
    # maximum recursion error will be raised
    def printListFromTailToHead(self, listNode):
        li = []
        if listNode:
            li.extend(self.printListFromTailToHead(listNode.next))
            li.append(listNode.val)
        return li


def test(solution):
    testcases = (
            [],  # empty linked list
            [1],  # only one node
            [1, 2, 3],  # simple list
            [1, 2, 2, 3],  # simple list with duplicated values
            offerhelper.gen_random_list(995, 0, 10000)  # large random linked list
            )

    for testcase in testcases:
        head = offerhelper.create_linked_list(testcase)
        assert solution.printListFromTailToHead(head) == testcase[::-1]


def bench_mark():
    solution = Solution()
    solution1 = Solution1()
    solution2 = Solution2()
    solution3 = Solution3()

    # head = offerhelper.create_linked_list([1, 2, 3])
    # solution1.printListFromTailToHead(head)

    test(solution)
    test(solution)
    test(solution)
    test(solution)

    print("All testcases pass")


if __name__ == '__main__':
    bench_mark()

