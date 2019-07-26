"""
File:         32_1_PrintFromTopToBottom.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  
"""
from queue import Queue

import offerhelper
from offerhelper import TreeNode


class Solution:
    def PrintFromTopToBottom(self, root):
        if not root:
            return []

        q = Queue()
        li = []
        q.put(root)

        while not q.empty():
            root = q.get()
            li.append(root.val)
            print(root.val)
            if root.left:
                q.put(root.left)
            if root.right:
                q.put(root.right)
        return li


def test(solution):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    solution.PrintFromTopToBottom(root)
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()

