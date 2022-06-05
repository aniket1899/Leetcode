class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dcopy = digits
        i=len(digits)-1
        while i>=0 and digits[i]==9:
            i-=1
        
        if i == len(digits)-1:
            tmp = digits[i] + 1
            return digits[:i] + [tmp]
        else:
            zeros = [0]*(len(digits)-1-i)
            
            if i >= 0:
                digits[i] += 1
                return digits[:i+1] + zeros
            else:
                return [1]+zeros
        
        
#         num = int(''.join([str(d) for d in digits]))
        
#         num +=1
        
#         arr = [int(n) for n in str(num)]
        
#         return arr


        
    
        