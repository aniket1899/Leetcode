from collections import defaultdict
import numpy as np

class Solution:
    def checkDuplicates(self, string):
        ctr = Counter()
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # board = np.array(board)
        
        rowsDict = defaultdict(list)
        colsDict = defaultdict(list)
        
        # colsDict = {i for i in range(N)}
        for rowTL in range(0, N, 3):
            
            for colTL in range(0, N, 3):
                cellsDict = []
                
                for i in range(3):
                    for j in range(3):
                        if board[rowTL+i][colTL+j] != '.':
                            elem = board[rowTL+i][colTL+j]
                            if elem in rowsDict[rowTL+i]:
                                # print(rowTL+i, colTL+j)
                                # print('rowsDict', rowsDict[rowTL+i])
                                return False
                            else:
                                rowsDict[rowTL+i].append(elem)
                            
                            if elem in colsDict[colTL+j]:
                                # print(rowTL+i, colTL+j)
                                # print('colsDict',colsDict[colTL+j])
                                return False
                            else:
                                colsDict[colTL+j].append(elem)
                            
                            if elem in cellsDict:
                                # print(rowTL+i, colTL+j)
                                # print('cellsDict',cellsDict)
                                return False
                            else:
                                cellsDict.append(elem)
                    
        return True
                
                
                
            