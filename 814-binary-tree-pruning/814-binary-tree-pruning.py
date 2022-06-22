# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def prune(self, node):
        
        if node.left and self.prune(node.left):
            node.left = None
        if node.right and self.prune(node.right):
            node.right = None
        
        if node.val == 0 and node.left is None and node.right is None:
            return True
        
        return False
            
            
        
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if self.prune(root):
            root = None
        
        return root
        