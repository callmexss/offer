"""
File:         31_IsPopOrder.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  
"""
import offerhelper


class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        pop_loc = 0
        for each in pushV:
            if each == popV[pop_loc]:
                pop_loc += 1
            else:
                stack.append(each)

        while stack:
            if stack[-1] == popV[pop_loc]:
                stack.pop()
                pop_loc += 1
            else:
                return False

        return not stack

def test(solution):
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()

