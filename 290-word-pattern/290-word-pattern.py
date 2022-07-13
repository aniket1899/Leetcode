from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern) or len(set(pattern)) != len(set(s)):
            return False
        patmap = defaultdict(lambda: None)
        for i in range(len(s)):
            if patmap[pattern[i]]:
                if patmap[pattern[i]] != s[i]:
                    return False
                
            else:
                patmap[pattern[i]] = s[i]
                
        return True
        