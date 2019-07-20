"""
File:         26_HasSubtree.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  
"""
import offerhelper
from offerhelper import TreeNode


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        return (self.isSubtreeWithRoot(pRoot1, pRoot2) or
                self.isSubtreeWithRoot(pRoot1.left, pRoot2) or
                self.isSubtreeWithRoot(pRoot1.right, pRoot2))

    def isSubtreeWithRoot(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return (self.isSubtreeWithRoot(pRoot1.left, pRoot2.left) and
                self.isSubtreeWithRoot(pRoot1.right, pRoot2.right))


def test(solution):
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()

