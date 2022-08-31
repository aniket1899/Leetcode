class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        counter = 0
        
        if dividend<0:
            dvd_neg = -1
        else:
            dvd_neg = 1
        
        if divisor<0:
            dvs_neg = -1
        else:
            dvs_neg = 1
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if divisor == 1:
            counter = dividend
        else:
            while  dividend >= divisor:
                dividend -= divisor
                counter += 1
            
        if dvd_neg == -1:
            counter = - counter
        if dvs_neg == -1:
            counter = - counter
        if counter > 2147483647:
            counter = 2147483647
        return counter
        