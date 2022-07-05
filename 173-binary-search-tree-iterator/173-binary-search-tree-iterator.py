# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def exploreLeft(self, node, stk):
        while node:
            stk.append(node)
            node = node.left
        return stk
    
    def __init__(self, root: Optional[TreeNode]):
        self.stk = self.exploreLeft(root, [])
        
        return None

    def next(self) -> int:
        # print([s.val for s in self.stk])
        curr = self.stk.pop()
        tmpnode = curr.right
        if tmpnode:
            self.stk.append(tmpnode)
            self.stk = self.exploreLeft(tmpnode.left, self.stk)
        # print([s.val for s in self.stk])
        # print('===')
        return curr.val
            
    def hasNext(self) -> bool:
        # print(self.stk[-1])
        return len(self.stk) > 0 #and self.stk[-1].right is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()