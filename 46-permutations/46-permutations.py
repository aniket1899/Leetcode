class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        fringe = [[n] for n in nums]
        if len(nums) == 1:
            return fringe
        perms = []
        N = len(nums)
        while fringe:
            temp_perm = fringe.pop()
            
            # for n in nums:
            #     if n not in temp_perm:
            #         temp_perm.append(n)
            temp_perm_combos = [temp_perm+[n] for n in nums if n not in temp_perm]
            for t in temp_perm_combos:
                if len(t) == N:
                    perms.append(t)
                else:
                    fringe.append(t)
                    # break
                    
        return perms
                    