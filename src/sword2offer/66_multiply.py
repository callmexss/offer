from functools import reduce

import offerhelper


class Solution:
    def multiply(self, A):
        # write code here
        B = [0] * len(A)

        for i in xrange(len(A)):
            B[i] = reduce(lambda x, y: x * y,
                          [A[j] for j in range(len(A)) if i != j])

        return B

class Solution1:
    def multiply(self, A):
        # write code here
        B = [0] * len(A)

        product = 1
        for i in xrange(len(A)):
            B[i] = product
            product *= A[i]
            
        product = 1
        for i in xrange(len(A)):
            B[~i] *= product
            product *= A[~i]

        return B


def test(solution):
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()

