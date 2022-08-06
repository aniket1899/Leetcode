class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # zeroRows = set()
        zeroCols = set()
        M, N = len(matrix), len(matrix[0])
        for row in range(M):
            flag = False
            for col in range(N):
                if matrix[row][col] == 0:
                    # zeroRows.add(row)
                    zeroCols.add(col)
                    flag = True
                
            if flag:
                matrix[row] = [0]*N
                    
                    
        for col in zeroCols:
            for row in range(M):
                matrix[row][col] = 0
                            
                        