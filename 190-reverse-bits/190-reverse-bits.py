class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = '0'*(32-len(binary)) + bin(n)[2:]
        return int(binary[::-1], 2)