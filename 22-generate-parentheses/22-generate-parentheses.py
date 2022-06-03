class Solution:
    
#     def addParanthesis(self, n, paran, open_paran):
        
#          if panran == '(':
#             if open_paran == n:
                
#                 open_paran
        
    def generateParenthesis(self, n: int) -> List[str]:
        
        fringe = []
        paran = set([])
        fringe.append(('(', 1, 1, 0)) # current str, open paran, all opened, all closed
        while fringe:
            currStr, currOpen, allOpen, allClosed = fringe.pop()
            if n == allClosed:
                paran.add(currStr)
                
            elif allOpen <= n:
                
                fringe.append((currStr+'(', currOpen + 1, allOpen + 1, allClosed))
                
                if currOpen > 0:
                    fringe.append((currStr+')', currOpen - 1, allOpen, allClosed+1))
                    
                    
        return list(paran)
                