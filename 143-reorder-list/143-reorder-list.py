from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reorder(self, prev, node, insertNode, idx):
        if not node:
            return insertNode, idx
        
        ins, maxIdx = self.reorder(node, node.next, insertNode, idx+1)
        if idx > maxIdx // 2:
            tmp = ins.next 
            ins.next = node
            prev.next = node.next
            node.next = tmp

            return tmp, maxIdx
        else:
            return  node, maxIdx
        # ... = self.reorder(node.next)
        
        
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.reorder(None, head, head, 0)
     