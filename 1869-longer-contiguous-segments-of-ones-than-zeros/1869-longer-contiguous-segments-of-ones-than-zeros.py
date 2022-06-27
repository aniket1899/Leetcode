class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        pat1s = re.compile(r'[1]+')
        pat0s = re.compile(r'[0]+')
        
        count1s = re.findall(pat1s, s)
        count0s = re.findall(pat0s, s)
        
        if not count1s:
            return False
        elif not count0s:
            return True
        
        if max([len(l) for l in count1s]) > max([len(l) for l in count0s]):
            return True
        else:
            return False