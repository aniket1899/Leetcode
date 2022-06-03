# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNode(self, prevNode, node, head):
        if node == None or node.next == None:
            return head
        
        pnode = node
        nnexnex = node.next.next
        if prevNode != None:
            # print(node.value)
            prevNode.next = node.next
            temp = node.next.next
            node.next.next = node
            node.next = temp
            return self.swapNode(pnode, nnexnex, head)
        else:
            head = node.next
            node.next = node.next.next
            head.next = node
            return self.swapNode(pnode, nnexnex, head)
        
        
        
        
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.swapNode(None, head, head)
        
        
        
        return head
        