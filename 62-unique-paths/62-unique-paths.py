class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # [[1 1 1]
        #  [1 2 3]
        #  [1 3 6]]
        
        paths = [[1 if i==0 or j==0 else 0 for i in range(n)] for j in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                paths[r][c] = paths[r-1][c] + paths[r][c-1]
        
        return paths[-1][-1]