class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        common = []
        max_val = 0
        max_coor = None
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        for i in range(len(nums1)):
            # tmp = []
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    common.append(nums1[i])
                    # if i-1>=0 and j-1>0:
                    #     tmp.append(1+dp_array[i-1][j-1])
                    # else:
                    #     tmp.append(1)
                    # if max_val < tmp[-1]:
                    #     max_val = tmp[-1]
                    #     max_coor = (i, j)
                # else:
                #     tmp.append(0)
            # dp_array.append(tmp)
        return common
#         print(dp_array)
#         if max_val > 0:
#             end1, end2 = max_coor
#             i, j = max_coor
#             while (i>=0 and j >= 0) and (dp_array[i][j] > 0):
#                 i-=1
#                 j-=1
#             start1, start2 = i+1, j+1
            
#             return nums1[start1:end1+1]
#         return []

                
        
                    
                