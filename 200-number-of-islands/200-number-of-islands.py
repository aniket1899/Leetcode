class Solution:
    def validStates(self, i, j, grid, M, N):
        states = []
        if i-1 >= 0:
            states.append((i-1, j))
        if i+1 < M:
            states.append((i+1, j))
        if j-1 >= 0:
            states.append((i, j-1))
        if j+1 < N:
            states.append((i, j+1))
        
        return states
            
        
            
    def numIslands(self, grid: List[List[str]]) -> int:
        
        M, N = len(grid), len(grid[0])
        visited = [[0 for _ in range(N)] for _ in range(M)]
        areas = 0
        
        for i in range(M):
            for j in range(N):
                if visited[i][j] or grid[i][j] == "0":
                    continue
                
                #bfs
                
                fringe = [(i, j)]
                area = []
                
                while fringe:
                    curr_i, curr_j = fringe.pop(0)
                    if visited[curr_i][curr_j]:
                        continue
                    area.append((curr_i, curr_j))
                    visited[curr_i][curr_j] = 1
                    for nexti, nextj in self.validStates(curr_i, curr_j, grid, M, N):
                        # print((nexti, nextj))
                        if visited[nexti][nextj] or grid[nexti][nextj] == "0":
                            continue
                        fringe.append((nexti, nextj))
                    
                areas += 1
        return areas
        
             # [["1","1","0","0","0"],
            #  ["1","1","0","0","0"],
            #  ["0","0","1","0","0"],
            #  ["0","0","0","1","1"]]       
                        