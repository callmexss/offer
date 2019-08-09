import offerhelper


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1

        li = list(range(n))
        cur = 0
        while len(li) > 1:
            for i in range(1, m):
                cur += 1
                if cur == len(li):
                    cur = 0
            li.remove(li[cur])
            if cur == len(li):
                cur = 0
        return li[0]


def test(solution):
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()
    Solution().LastRemaining_Solution(10, 3)
