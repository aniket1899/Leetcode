from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        fringe = deque([(root, 1)])
        
        while fringe:
            tmp = deque([])
            for i in range(len(fringe)):
                curr, depth = fringe.popleft()
                if not (curr.left or curr.right):
                    return depth
                else:
                    if curr.right:
                        tmp.append((curr.right, depth+1))
                    if curr.left:
                        tmp.append((curr.left, depth+1))
            fringe = tmp
        return depth
        
#         while fringe:
#             curr, depth = fringe.popleft()
#             if not (curr.left or curr.right):
#                 return depth
            
#             else:
#                 if curr.right:
#                     fringe.append((curr.right, depth+1))
#                 if curr.left:
#                     fringe.append((curr.left, depth+1))
                    
#         return depth
        
            
    