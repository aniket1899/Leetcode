class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end = 0, len(s) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        startVowel, endVowel = None, None
        s = [ch for ch in s]
        
        while start < end:
            if startVowel is not None and endVowel is not None:
                s[startVowel], s[endVowel] =  s[endVowel], s[startVowel]
                startVowel, endVowel = None, None
                start += 1
                end -= 1
                
            if startVowel or s[start].lower() in vowels:
                startVowel = start
            else:
                startVowel = None
                start += 1
            
            if endVowel or s[end].lower() in vowels:
                endVowel = end
            else:
                endVowel = None
                end -= 1
                
        
        return ''.join(s)