class Solution:
    def hammingWeight(self, n: int) -> int:
        countOnes = 0
        # print(n)
        while n > 0:
            # print(n)
            if n % 2:
                countOnes += 1
            n = n // 2
        
        return countOnes