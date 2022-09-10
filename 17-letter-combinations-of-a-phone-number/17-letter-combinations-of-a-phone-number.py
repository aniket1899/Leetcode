from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        alpha = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        fringe = deque([(a, 0) for a in alpha[digits[0]]])
        
        target = len(digits)-1
        combinations = []
        
        while fringe:
            curr, idx = fringe.popleft()
            if idx == target:
                combinations.append(curr)
                continue
            idx += 1
            
            for nxt in alpha[digits[idx]]:
                fringe.append((curr + nxt, idx))
                
        return combinations
                