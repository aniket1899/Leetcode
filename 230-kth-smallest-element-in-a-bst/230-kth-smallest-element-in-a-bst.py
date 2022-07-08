# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findkthSmallest(self, node, k):
        if not node:
            return []
        
        if not (node.left or node.right):
            return [node.val]
        
        res  = self.findkthSmallest(node.left, k) + [node.val] + self.findkthSmallest(node.right, k)
        # print(res)
        return res
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.findkthSmallest(root, k)[k-1]