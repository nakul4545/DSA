# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        # If left is none return right 
        if root.left is None:
            return 1 + self.minDepth(root.right)
        # if right is none return left
        if root.right is None:
            return 1 + self.minDepth(root.left)
        # Also we can add one condn for leaf but anyways it is going to handled by l_d and r_d min code
        # if root.left is None and root.right is None:
        #     return 1 # Or the following code doing the same return 1+min(0,0)
        # If both are not null return min
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        # Now take min of both 
        return 1 + min(left_depth, right_depth)
        