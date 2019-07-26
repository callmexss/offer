import re


# class Solution:
#     def isNumeric(self, s):
#         return re.match(r'^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$', s)


class Solution:
    def isNumeric(self, s):
        matched =  re.fullmatch(r'^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$', s)
        if matched:
            return matched.group() is not ''
        else:
            return False


def test(solution):
    testcases = (
            ("123", True),
            ("0.123", True),
            ("+1", True),
            ("-2", True),
            ("-1E-16", True),
            ("", False),
            ("abc", False),
            ("12e", False),
            # ("1e.213", False),
            # ("-1.e213", False),
            )

    for testcase in testcases:
        assert solution.isNumeric(testcase[0]) == testcase[1],\
               f"{testcase} failed, "\
               f"output {solution.isNumeric(testcase[0])} != {testcase[1]}"


def bench_mark():
    solution = Solution()
    test(solution)


if __name__ == '__main__':
    bench_mark()

