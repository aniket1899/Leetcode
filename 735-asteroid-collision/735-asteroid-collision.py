class Solution:
    # def checkAll(self, l):
    #     return all(l>0) or all(l<0)
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        uncol = asteroids[:2]
        i = 2
        N = len(asteroids)
        while i <= N:
            if len(uncol) >= 2:
                last = uncol[-1]
                seclast = uncol[-2]
                if last < 0 and seclast > 0:
                    uncol.pop()
                    uncol.pop()
                    
                    if abs(last) == abs(seclast):
                        if i < N:
                            uncol.append(asteroids[i])
                        i += 1
                    elif abs(last) > abs(seclast):
                        uncol.append(last)
                    else:
                        uncol.append(seclast)
                else:
                    if i < N:
                        uncol.append(asteroids[i])
                    i += 1 
            else:
                if i < N:
                    uncol.append(asteroids[i])
                i += 1
        
        return uncol
                        
                        
                
