import offerhelper

from offerhelper import TreeLinkNode


class Solution:
    def GetNext(self, pNode):
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        else:
            while pNode.next:
                parent = pNode.next
                if parent.left == pNode:
                    return parent
                pNode = pNode.next

        return None


def test(solution):
    # testcases
    # [], None
    # [1], Node
    pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()
