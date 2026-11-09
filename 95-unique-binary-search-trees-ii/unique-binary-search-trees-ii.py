# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def build(low: int, high: int) -> list[TreeNode | None]:
            if low > high:
                return [None]

            trees = []
            for value in range(low, high + 1):
                left_trees = build(low, value - 1)
                right_trees = build(value + 1, high)

                for left in left_trees:
                    for right in right_trees:
                        trees.append(TreeNode(value, left, right))

            return trees

        return build(1, n)
