from collections import defaultdict
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        valid  = set([i+1 for i in range(len(matrix))])

        for row, col in zip(matrix, zip(*matrix)):
            if set(row) != valid or set(col) != valid:
                return False
            
#         colAdditions = defaultdict(list)
#         for row in matrix:
#             if set(row) != rowAddition:
#                 return False
            
#             for k in range(len(row)):
#                 colAdditions[k].append(row[k])
        
            
#         for idx, coladd in colAdditions.items():
#             if set(coladd) != rowAddition:
#                 return False
        
        return True
        