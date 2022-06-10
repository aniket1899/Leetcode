# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head 
        while node:
            lastVal = node.val
            lastNode = node
            node= node.next
            while node and node.val == lastVal:
                node= node.next
            
            lastNode.next  = node

            
        return head
            
        