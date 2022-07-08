class Solution:
    def validStates(self, i, j, board, M, N):
        states = []
        if i - 1 >= 0:
            states.append((i-1, j))
        if i + 1 < M:
            states.append((i+1, j))
        if j - 1 >= 0:
            states.append((i, j-1))
        if j + 1 < N:
            states.append((i, j+1))
        return states
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        areas = 0
        M, N = len(board), len(board[0])
        visited = [[0 for _ in range(N)] for _ in range(M)]
        
        
        for i in range(M):
            for j in range(N):
                if board[i][j]  == 'X' or visited[i][j]:
                    continue
                
                # else bfs
                
                    
                # print(i, j)
                fringe = [(i, j)]
                areasTBC = []
                if i in [0, M-1]  or j in [0, N-1]:
                    void = True
                else:
                    void = False
                    
                while fringe:
                    curri, currj = fringe.pop(0)
                    if board[curri][currj]  == 'X' or visited[curri][currj]:
                        continue
                    areasTBC.append((curri, currj))
                    visited[curri][currj] = 1
                    nextStates = self.validStates(curri, currj, board, M, N)
                    for nexti, nextj in nextStates:
                        # if board[nexti][nextj]  == 'X' or visited[nexti][nextj]:
                        #     continue
                        if (nexti in [0, M-1]  or nextj in [0, N-1]) and board[nexti][nextj] == 'O':
                            void = True
                            # break
                        
                        
                        fringe.append((nexti, nextj))
                    
                if not void:
                    for posi, posj in areasTBC:
                        board[posi][posj] = 'X'
                    
        return None
                  
# [["O","O","O","O","X","X"],
#  ["O","O","O","O","O","O"],
#  ["O","X","O","X","O","O"],
#  ["O","X","O","O","X","O"],
#  ["O","X","O","X","O","O"],
#  ["O","X","O","O","O","O"]]
                        
# [["O","O","O","O","X","X"],
#  ["O","O","O","O","O","O"],
#  ["O","X","O","X","O","O"],
#  ["O","X","O","X","X","O"],
#  ["O","X","O","X","O","O"],
#  ["O","X","O","O","O","O"]]