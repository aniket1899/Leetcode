class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # solution #2
        
        products = []
        prod = 1
        for num in nums:
            products.append(prod)
            prod *= num
        
        print(products)
        
        prod = 1
        for i in reversed(range(len(nums))):
            products[i] *= prod
            prod *= nums[i]
            
            
        return products
            
            
            
            
            
        # solution #1
#         prod = 1
#         prodZero = 1
#         zeros = 0
#         for n in nums:
#             if n == 0:
#                 zeros += 1
#                 prodZero = prod
#             else:
#                 prodZero *= n
#             prod *= n
        
#         res = []
        
#         for n in nums:
#             if n == 0:
#                 res.append(prodZero)
#             else:
#                 res.append(prod//n)
#         return res
            