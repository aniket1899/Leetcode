from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern) or len(set(pattern)) != len(set(s)):
            return False
        patmap = defaultdict(lambda: None)
        for i in range(len(s)):
            if patmap[s[i]]:
                if patmap[s[i]] != pattern[i]:
                    return False
                
            else:
                patmap[s[i]] = pattern[i]
                
        return True
        