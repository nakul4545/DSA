# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []
        level = 0 # To keep the track of level so how to push the elemenets of that level
        while q:
            lvl_size = len(q)
            tmp = []

            for _ in range(lvl_size):
                node = q.popleft()
                if level %2 == 0:
                    tmp.append(node.val) # Left to Right
                else:
                    tmp.insert(0, node.val) # Right to Left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lvl_size -= 1
            level += 1
            res.append(tmp)
        return res

       

