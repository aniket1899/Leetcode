from collections import deque
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        fringe = deque([(str(i)) for i in range(1, 10)])
        valid = set()
        
        while fringe:
            curr = fringe.popleft()
            
            if len(curr) == n:
                valid.add(int(curr))
                continue
                
            lastbit = int(curr[-1])
            
            if lastbit - k >= 0:
                fringe.append(curr+str(lastbit - k))
            if lastbit + k <= 9:
                fringe.append(curr+str(lastbit + k))
                
        return list(valid)
            