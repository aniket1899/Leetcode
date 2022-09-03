class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal = [[1]]
        for i in range(2,numRows+1):
            row = [1]*i
            for j in range(1, i-1):
                row[j] = pascal[-1][j-1] + pascal[-1][j]
                
            pascal.append(row)
        
        return pascal
                