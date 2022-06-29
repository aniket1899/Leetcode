# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addLeftRight(self, node, strnum):
        if not (node.left or node.right):
            return int(strnum + str(node.val))
        
        left, right = 0, 0
        if  node.left:
            left = self.addLeftRight(node.left, strnum + str(node.val))
            
        if  node.right:
            right = self.addLeftRight(node.right, strnum + str(node.val))
        # print(left, right)
        # print("===")
        # if left and right:
        return int(left) + int(right)
        # else:
        #     return left or right
        
        
        
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.addLeftRight(root, "")