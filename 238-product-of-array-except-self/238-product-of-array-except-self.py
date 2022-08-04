class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prodZero = 1
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1
                prodZero = prod
            else:
                prodZero *= n
            prod *= n
        
        res = []
        
        for n in nums:
            if n == 0:
                res.append(prodZero)
            else:
                res.append(prod//n)
        return res
            