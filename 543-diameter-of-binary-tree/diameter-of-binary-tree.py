# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node is None:
                return 0
            left_depth = height(node.left)
            right_depth = height(node.right)
            if left_depth + right_depth > max_dia[0]:
                max_dia[0]= left_depth + right_depth
            return 1+ max(left_depth, right_depth)

        max_dia = [0]
        height(root)
        return max_dia[0]

