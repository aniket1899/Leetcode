class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k%N
        # nums = nums[-k:] + nums[:-k-1]
        # tmp = nums.copy()
        # nums = []
        # nums = tmp[N-k-1:] + tmp[:N-k-1]
        
        # for _ in range(k):
        #     tmp = nums.pop()
        #     nums.insert(0, tmp)
        
        if k <= N - k:
            for _ in range(k):
                tmp = nums.pop()
                nums.insert(0, tmp)
        else:
            for _ in range(N-k):
                tmp = nums.pop(0)
                nums.append(tmp)
        # print(nums)