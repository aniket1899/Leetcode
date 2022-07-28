from collections import defaultdict
import numpy as np

class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Method #1
#         N = 9
#         # board = np.array(board)
        
#         rowsDict = defaultdict(list)
#         colsDict = defaultdict(list)
        
#         # colsDict = {i for i in range(N)}
#         for rowTL in range(0, N, 3):
            
#             for colTL in range(0, N, 3):
#                 cellsDict = []
                
#                 for i in range(3):
#                     for j in range(3):
#                         if board[rowTL+i][colTL+j] != '.':
#                             elem = board[rowTL+i][colTL+j]
#                             if elem in rowsDict[rowTL+i]:
#                                 # print(rowTL+i, colTL+j)
#                                 # print('rowsDict', rowsDict[rowTL+i])
#                                 return False
#                             else:
#                                 rowsDict[rowTL+i].append(elem)
                            
#                             if elem in colsDict[colTL+j]:
#                                 # print(rowTL+i, colTL+j)
#                                 # print('colsDict',colsDict[colTL+j])
#                                 return False
#                             else:
#                                 colsDict[colTL+j].append(elem)
                            
#                             if elem in cellsDict:
#                                 # print(rowTL+i, colTL+j)
#                                 # print('cellsDict',cellsDict)
#                                 return False
#                             else:
#                                 cellsDict.append(elem)
                    
#         return True
                
            # Method #2
            N = 9
            rowctr = [set() for _ in range(N)]
            colctr = [set() for _ in range(N)]
            cellctr = [[set() for _ in range(N//3)] for _ in range(N//3)]

            for row in range(N):
                for col in range(N):
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in rowctr[row]:
                        # print(row, col)
                        # print('row', rowctr[row])
                        return False
                    else:
                        rowctr[row].add(board[row][col])

                    if board[row][col] in colctr[col]:
                        # print(row, col)
                        # print('row', rowctr[row])
                        return False
                    else:
                        colctr[col].add(board[row][col])

                    if board[row][col] in cellctr[row//3][col//3]:
                        # print(row, col)
                        # print('row', rowctr[row])
                        return False
                    else:
                        cellctr[row//3][col//3].add(board[row][col])
            return True