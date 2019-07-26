import offerhelper

from offerhelper import TreeNode


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None

        if len(pre) == len(tin) == 1:
            return TreeNode(pre[0])

        root = TreeNode(pre[0])
        root_index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:root_index+1], tin[:root_index])
        root.right = self.reConstructBinaryTree(pre[root_index+1:], tin[root_index+1:])
        return root


        

def test(solution):
    testcases = (
            ([], [], []),
            ([1], [], None),
            ([], [1], None),
            ([1], [1], [1]),
            ([1, 2, 3], [3, 2, 1], [3, 2, 1]),
            ([1, 2, 3], [1, 2, 3], [3, 2, 1]),
            ([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6], [7, 4, 2, 5, 8, 6, 3, 1]),
            )

    for testcase in testcases:
        root = Solution().reConstructBinaryTree(*testcase[:2])
        if not root:
            assert not testcase[-1]
        else:
            assert offerhelper.post_order(root) == testcase[-1],\
                   f"{testcase} failed"


def bench_mark():
    solution = Solution()

    test(solution)


if __name__ == '__main__':
    bench_mark()

