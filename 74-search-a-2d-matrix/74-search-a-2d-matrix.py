class Solution:
    def translate_2D(self, row, col, NCOLS):
        return (row) * NCOLS + col
        
    def translate_1D(self, NROWS, NCOLS, idx):
        return  idx // NCOLS, idx % NCOLS
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        NROWS = len(matrix)
        NCOLS =  len(matrix[0])
        
        
        l, h = 0, self.translate_2D(NROWS-1, NCOLS-1, NCOLS)
        
        # print(h)
        # print(self.translate_1D(NROWS, NCOLS, 10))
        
        while l <= h:
            mid = (l+h)//2
            r, c = self.translate_1D(NROWS, NCOLS, mid)
            # print('---')
            # print(l, h)
            # print(mid)
            # print(r, c)
            mid_value = matrix[r][c]
            if mid_value == target:
                return True
            if mid_value < target:
                l = mid + 1
            else:
                h = mid - 1
                
        return False
            