"""
File:         27_Mirror.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  
"""
import offerhelper
from offerhelper import TreeNode


class Solution:
    def Mirror(self, root):
        if not root:
            return root

        # swap left subtree and right subtree
        node = root.left
        root.left = root.right
        root.right = node

        self.Mirror(root.left)
        self.Mirror(root.right)

        return root


def test(solution):
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()

