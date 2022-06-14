# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, node):
        if not node:
            return 0
        else:
            return max(self.depth(node.left), self.depth(node.right)) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        node = root
        if abs(self.depth(node.left)  - self.depth(node.right)) < 2 and \
        self.isBalanced(node.left) and self.isBalanced(node.right):
            return  True
        else:
            return False
            
        
        
#         nodes = [root] # nodes at the same level
#         depth = None
#         while nodes:
#             tmp = []
            
#             for node in nodes:
#                 if node.left or node.right:
#                     if not depth:
#                         depth = 0
#                     elif depth == 0:
#                         depth += 1
#                     elif depth == 1:
#                         return False
                    
#                     if node.left:
#                         tmp.append(node.left)
#                     if node.right:
#                         tmp.append(node.right)
                    
#             nodes = tmp
                
            
#         return True


                        
                    
                    