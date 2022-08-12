from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if  not root:
            return 0
        nodes = deque([root])
        depth = 0
        while nodes:
            levlen = len(nodes)
            
            for _ in range(levlen):
                curr = nodes.popleft()
                if curr.left: 
                    nodes.append(curr.left)
                if curr.right: 
                    nodes.append(curr.right)
            
            depth += 1
            
        return depth
            
            
                