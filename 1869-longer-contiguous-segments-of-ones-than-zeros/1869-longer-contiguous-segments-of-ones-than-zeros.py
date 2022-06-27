class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count = {0:0, 1:0}
        tmp0 = 0
        tmp1 = 0
        for ch in s:
            if ch == '0':
                tmp1 = 0
                tmp0 += 1
                count[0] = max(count[0], tmp0)
            else:
                tmp0 = 0
                tmp1 += 1
                count[1] = max(count[1], tmp1)
        print(count[1] , count[0])
        return count[1] > count[0]
#         pat1s = re.compile(r'[1]+')
#         pat0s = re.compile(r'[0]+')
        
#         count1s = re.findall(pat1s, s)
#         count0s = re.findall(pat0s, s)
        
#         if not count1s:
#             return False
#         elif not count0s:
#             return True
        
#         if max([len(l) for l in count1s]) > max([len(l) for l in count0s]):
#             return True
#         else:
#             return False