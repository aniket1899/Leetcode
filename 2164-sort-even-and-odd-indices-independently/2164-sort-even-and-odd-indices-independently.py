class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        print(len(nums))
        odd = [0]*(len(nums)//2)
        even = [0]*((len(nums)+1)//2)
        i, k = 0, 0
        while i < len(nums)-1:
            even[k] = nums[i]
            odd[k] = nums[i+1]
            i += 2
            k += 1
        
        if len(nums)%2 == 1:
            even[-1] = nums[-1]
        print(even, odd)
        
        even.sort()
        odd.sort(reverse = True)
        # print(even, odd)
        i = 0
        for e, o in zip(even[:len(nums)//2], odd):
            nums[i] = e
            nums[i+1] = o
            i+=2
        if len(nums)%2 == 1:
             nums[-1] = even[-1]
        return nums
            