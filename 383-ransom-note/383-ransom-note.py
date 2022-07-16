from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ctrRansom = Counter(ransomNote)
        ctrMagazine = Counter(magazine)
        
        for key, val in ctrRansom.items():
            if ctrMagazine[key] < val:
                return False
            
        return True