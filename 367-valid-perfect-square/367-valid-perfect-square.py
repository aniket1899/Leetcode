class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return True
        # for i in range(num):
        #     sq = i*i
        #     print(sq, num)
        #     if sq == num:
        #         return True
        #     elif sq > num:
        #         return False
        l, r = 2, num
        
        
        while l<= r:
            mid = (l+r) // 2
            tmp = mid*mid
            if tmp == num:
                return True
            elif tmp < num:
                l = mid + 1
            else:
                r = mid - 1
                
        return False
                
        
        