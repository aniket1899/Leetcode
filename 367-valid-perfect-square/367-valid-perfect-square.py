class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return num
        for i in range(num):
            sq = i*i
            print(sq, num)
            if sq == num:
                return True
            elif sq > num:
                return False
        
        