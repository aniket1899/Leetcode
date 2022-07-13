class Solution:
    def hammingWeight(self, n: int) -> int:
        # countOnes = 0
        # while n > 0:
        #     # print(n)
        #     if n % 2:
        #         countOnes += 1
        #     n = n // 2
        # print(bin(n))
        return bin(n)[2:].count('1')