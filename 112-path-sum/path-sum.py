# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def fun(node, remaining):
            if node is None:
                return False
            remaining -= node.val
            if node.left is None and node.right is None: # Means it is leaf
                # return remaining == 0
                if remaining == 0:
                    return True
                else:
                    return False
            return fun(node.left, remaining) or fun(node.right, remaining) # Means True or False 
            # Let's say one root is saying no remaining is not 0 means oath sum is not 0 and another
            # is 0 so final answer wowuld be 0 

        return fun(root, targetSum)