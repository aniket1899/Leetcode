class Solution:
    def addDigits(self, num: int) -> int:
        total = str(num)
        while (len(total)) > 1:
            tmp = 0
            for n in total:
                tmp += int(n)
            total = str(tmp)
        return int(total)