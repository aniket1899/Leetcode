# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        T, B, L, R = 0, m-1, 0, n-1
        
        topflag, rightflag = True, True
        m_adj, n_adj = 1, 0
        i, j = 0, 0
        res = [[-1 for _ in range(n)] for _ in range(m)]
        node = head
        while node:
            if topflag:
                for _ in range(n-n_adj):
                    if not node:
                        return res
                    
                    res[i][j] = node.val
                    node = node.next
                    j+=1
                n_adj+=1
                j-=1
                i+=1
                for _ in range(m-m_adj):
                    if not node:
                        return res
                    # print(i, j)
                    res[i][j] = node.val
                    node = node.next
                    i+=1
                m_adj+=1
                j-=1
                i-=1
                topflag = not topflag
            else:
                for _ in range(n-n_adj):
                    if not node:
                        return res
                   
                    res[i][j] = node.val
                    node = node.next
                    j-=1
                n_adj+=1
                j+=1
                i-=1
                for _ in range(m-m_adj):
                    if not node:
                        return res
                    res[i][j] = node.val
                    node = node.next
                    i-=1
                m_adj+=1
                j+=1
                i+=1
                topflag = not topflag
            
        return res
            
                    