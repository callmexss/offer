"""
File:         30_minStack.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  
"""
import offerhelper


class Solution:
    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, node):
        if not self.data_stack:
            self.data_stack.append(node)
            self.min_stack.append(node)
        if node < self.min_stack[-1]:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])
        self.data_stack.append(node)

    def pop(self):
        if not self.data_stack:
            return
        self.data_stack.pop()
        self.min_stack.pop()

    def top(self):
        if not self.data_stack:
            return
        return self.data_stack[-1]

    def min(self):
        if not self.min_stack:
            return
        return self.min_stack[-1]

def test(solution):
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()

