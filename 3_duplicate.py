from __future__ import print_function

class Solution:
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        
        for i in range(len(numbers)):
            print(i, numbers[i])
            while numbers[i] != i:
                loc = numbers[i]
                if numbers[i] == numbers[loc]:
                    duplication[0] = numbers[i]
                    return True
                numbers[i], numbers[loc] = numbers[loc], numbers[i]
        return False



if __name__ == '__main__':
    dup = [0]
    ret = Solution().duplicate([2, 3, 1, 0, 2, 5, 3], dup)
    print(ret)

