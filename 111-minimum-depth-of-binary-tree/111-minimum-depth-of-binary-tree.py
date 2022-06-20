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
        fringe = [(root, 1)]
        
        while fringe:
            curr, depth = fringe.pop(0)
            if not (curr.left or curr.right):
                return depth
            
            else:
                if curr.right:
                    fringe.append((curr.right, depth+1))
                if curr.left:
                    fringe.append((curr.left, depth+1))
                    
        return depth