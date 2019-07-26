# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        flag = [False] * len(matrix)
        for i in range(rows):
            for j in range(cols):
                if self.judge(matrix, i, j, rows, cols, flag, path, 0):
                    return True
        
    def judge(self, matrix, i, j, rows, cols, flag, path, k):
        # index = i * rows + j -> bug is here!!!
        index = i * cols + j
        if (not matrix or i < 0 or j < 0 or i >= rows or j >= cols or
            matrix[index] != path[k] or flag[index]):
            return False

        if (k == len(path) - 1):
            return True

        flag[index] = True
        
        if (self.judge(matrix, i-1, j, rows, cols, flag, path, k+1) or
            self.judge(matrix, i+1, j, rows, cols, flag, path, k+1) or
            self.judge(matrix, i, j-1, rows, cols, flag, path, k+1) or
            self.judge(matrix, i, j+1, rows, cols, flag, path, k+1)):
            return True
        
        flag[index] = False
        return False
            

if __name__ == "__main__":
    li = [x for x in "abce"]
    print(Solution().hasPath(li, 2, 2, "ac"))

    li = [x for x in "abcesfcsadee"]
    print(Solution().hasPath(li, 3, 4, "bce"))

