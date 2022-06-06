# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        node= head
        prev = None
        prevLesserNode = None
        
        while node:
            if node.val < x:
                if prevLesserNode and prevLesserNode.next != node:
                    tmp = prevLesserNode.next
                    prevLesserNode.next = node
                    prev.next = node.next
                    node.next = tmp
                elif not prevLesserNode and head != node:
                    prev.next = node.next
                    node.next = head
                    head = node
                    
                prevLesserNode = node
                
            # else:
                
            prev = node 
            node = node.next
            
        return head