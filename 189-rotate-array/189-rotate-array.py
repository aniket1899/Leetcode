class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k%N
        
        nums[:] = nums[N-k:] + nums[:N-k]
        
        # for _ in range(k):
        #     tmp = nums.pop()
        #     nums.insert(0, tmp)
        
        # if k <= N - k:
        #     for _ in range(k):
        #         tmp = nums.pop()
        #         nums.insert(0, tmp)
        # else:
        #     for _ in range(N-k):
        #         tmp = nums.pop(0)
        #         nums.append(tmp)
        # print(nums)