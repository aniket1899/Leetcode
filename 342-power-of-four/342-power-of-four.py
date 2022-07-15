class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 1:
            return n == 1
        binary = list(reversed(bin(n)[2:]))
        # print(binary)
        return binary.count('1') == 1 and binary.index('1') % 2 == 0