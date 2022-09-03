class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1]]
        for i in range(2,rowIndex+2):
            row = [1]*i
            for j in range(1, i-1):
                row[j] = pascal[-1][j-1] + pascal[-1][j]
            pascal = [pascal[-1]]
            pascal.append(row)
        
        return pascal[-1]