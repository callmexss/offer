import unittest

import offerhelper
from offerhelper import TreeNode


class TreeTraverse(unittest.TestCase):
    def setUp(self):
        emptyTree = None
        oneElementTree = TreeNode(0)

        # ordinary tree
        ordinaryTree = TreeNode(0)
        ordinaryTree.left = TreeNode(1)
        ordinaryTree.right = TreeNode(2)

        # left only tree
        leftOnlyTree = TreeNode(0)
        leftOnlyTree.left = TreeNode(1)
        leftOnlyTree.left.left = TreeNode(2)

        # right only tree
        rightOnlyTree = TreeNode(0)
        rightOnlyTree.right = TreeNode(1)
        rightOnlyTree.right.right = TreeNode(2)


        self.Trees = (
                (emptyTree, [], [], []),
                (oneElementTree, [0], [0], [0]),
                (ordinaryTree, [0, 1, 2], [1, 0, 2], [1, 2, 0]),
                (leftOnlyTree, [0, 1, 2], [2, 1, 0], [2, 1, 0]),
                (rightOnlyTree, [0, 1, 2], [0, 1, 2], [2, 1, 0]),
                )

    def test_pre_order(self):
        for tree in self.Trees:
            self.assertEqual(offerhelper.pre_order(tree[0]), tree[1])

    def test_in_order(self):
        for tree in self.Trees:
            self.assertEqual(offerhelper.in_order(tree[0]), tree[2])

    def test_post_order(self):
        for tree in self.Trees:
            self.assertEqual(offerhelper.post_order(tree[0]), tree[3])


if __name__ == '__main__':
    unittest.main()
