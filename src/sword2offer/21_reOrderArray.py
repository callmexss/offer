class Solution:
    """O(n) O(n)"""
    def reOrderArray(self, array):
        if not array or len(array) <= 1:
            return array
        
        odds = [x for x in array if x & 1]
        evens = [x for x in array if x & 1 == 0]
        return odds+evens
        

class Solution1:
    def reOrderArray(self, array):
        for i in range(len(array) - 1, 0, -1):
            for j in range(0, i):
                if array[j] & 1 == 0 and array[j+1] & 1:
                    array[j], array[j+1] = array[j+1], array[j]
        return array
        

def test(solution):
    testcases = (
            ([], []),
            ([1], [1]),
            ([1, 2, 3], [1, 3, 2]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 3, 5, 7, 2, 4, 6]),
            ([2, 4, 6, 8, 1], [1, 2, 4, 6, 8]),
            )

    for testcase in testcases:
        array = testcase[0][:]
        ret = solution.reOrderArray(array)
        assert ret == testcase[1],\
               f"{testcase} failed: "\
               f"{ret} != {testcase[1]}"

def bench_mark():
    solution = Solution()
    solution1 = Solution1()

    test(solution)
    test(solution1)


if __name__ == '__main__':
    bench_mark()

