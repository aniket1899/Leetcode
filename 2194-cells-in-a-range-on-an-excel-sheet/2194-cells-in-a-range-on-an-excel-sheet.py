class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        L, R = s.split(':')
        sel = []
        row = min(ord(R[0]), ord(L[0]))
        col = min(int(R[1]), int(L[1]))
        for r in range(abs(ord(R[0]) - ord(L[0])) + 1):
            for c in range(abs(int(R[1]) - int(L[1])) + 1):
                sel.append(chr(row + r) + str(col + c))
                
        return sel