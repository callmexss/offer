"""
File:         28_isSymmetrical.py
Author:       callmexss
Email:        callmexss@126.com
Github:       https://github.com/callmexss
Description:  
"""
import offerhelper


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        root = pRoot
        symRoot = self.Mirror(root)
        if self.Equal(symRoot, pRoot):
            return True
        else:
            return False
        
    def Mirror(self, root):
        if not root:
            return root
        node = root.left
        root.left = root.right
        root.right = node
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
    
    def Equal(self, root1, root2):
        if not root1 and not root2:
            return True
        if (root1 and (not root2)) or ((not root1) and root2):
            return False
        
        if root1.val != root2.val:
            return False
        return self.Equal(root1.left, root2.left) and self.Equal(root1.right, root2.right)


class Solution1:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.judge(pRoot.left, pRoot.right)

    def judge(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False
        return (self.judge(root1.left, root2.right) and 
                self.judge(root1.right, root2.left))


def test(solution):
    testcases = ()

    for testcase in testcases:
        pass


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()

