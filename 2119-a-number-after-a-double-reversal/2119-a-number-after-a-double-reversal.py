class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = str(num)
        return not num[-1] == '0' or num == '0'
        