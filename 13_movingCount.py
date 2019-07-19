# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if not threshold or rows <= 0 or cols <= 0:
            return 0
        
        visited = [False for i in range(rows * cols)]
        return self.movingCountCore(threshold, rows, cols,
                                    0, 0, visited)
        
    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row * cols + col] = True
            
            count = (1 + self.movingCountCore(threshold, rows, cols,
                                              row-1, col, visited)
                       + self.movingCountCore(threshold, rows, cols,
                                              row, col-1, visited)
                       + self.movingCountCore(threshold, rows, cols,
                                              row+1, col, visited)
                       + self.movingCountCore(threshold, rows, cols,
                                              row, col+1, visited))
        return count
    
    def check(self, threshold, rows, cols, row, col, visited):
        if (row >= 0 and row < rows and col >= 0 and col < cols and
            self.getDigitSum(row) + self.getDigitSum(col) <= threshold and
            not visited[row * cols + col]):
            return True
        return False
    
    def getDigitSum(self, number):
        ret = 0
        while number > 0:
            ret += number % 10
            number /= 10
        return ret


if __name__ == "__main__":
    print(Solution().movingCount(4, 2, 2))

