# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        q = deque([root])
        null_seen = False 
        while q:
            node = q.popleft()
            if node is None:
                null_seen = True
                continue
            if null_seen: # Means null_seen is True and node is not none otherwise above condn got executed
                return False
            q.append(node.left)
            q.append(node.right)

        return True # If return False never executed means null_seen either became True or never became True but never became False that's why return True instead of returning null_seen
        

        