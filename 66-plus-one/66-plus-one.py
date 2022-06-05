class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = int(''.join([str(d) for d in digits]))
        
        num +=1
        
        arr = [int(n) for n in str(num)]
        
        return arr