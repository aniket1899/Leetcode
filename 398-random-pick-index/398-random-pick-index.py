from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.indices = defaultdict(list)
        for i, num in enumerate(self.nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        randomIndex = random.randrange(0, len(self.indices[target]))
        return self.indices[target][randomIndex]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)