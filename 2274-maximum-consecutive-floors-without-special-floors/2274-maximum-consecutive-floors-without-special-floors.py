class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        diff = max(special[0]-bottom, top-special[-1])
        prev = special[0]
        for num in special[1:]:
            diff = max(num-prev-1, diff)
            prev = num
        
        return diff if diff!=1 else 0