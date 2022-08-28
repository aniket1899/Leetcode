class Solution:
    def sortAndApply(self, mat, row, col, M, N):
        diag = []
        r, c = row, col
        while r<M and c<N:
            diag.append(mat[r][c])
            r += 1
            c += 1
        diag.sort()
        r, c, idx = row, col, 0
        while r<M and c<N:
            mat[r][c] = diag[idx]
            r += 1
            c += 1
            idx += 1
        return mat
            
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        M, N = len(mat), len(mat[0])
        
        for i in range(N):
            mat = self.sortAndApply(mat, 0, i, M, N)
        
        for i in range(1, M):
            mat = self.sortAndApply(mat, i, 0, M, N)
            
        return mat
            
        