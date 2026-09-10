# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# VERY NICE QUESTION 

from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case 
        if not root:
            return []
        
        q = deque([root]) # 3
        res = []
        while q:
            lvl_size = len(q)
            tmp = [] # After every level initiaalize to empty

            for _ in range(lvl_size):
                node = q.popleft()
                tmp.append(node.val) # Add val then check child nodes

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lvl_size -= 1 # Because loop should only run len(lvl_size) then jump to next lvl
            # Here lvl_size becomes 0 so append whatever is there in tmp    
            res.append(tmp)
        return res