# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def reverse(self, node):
#         if not node.next:
#             return node, node
        
#         nextNode, head = self.reverse(node.next)
#         nextNode.next = node
        
#         return node, head
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head:
        #     node, head =  self.reverse(head)
        #     node.next = None
        #     return head
        
        node = head
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        return prev
        
        
        