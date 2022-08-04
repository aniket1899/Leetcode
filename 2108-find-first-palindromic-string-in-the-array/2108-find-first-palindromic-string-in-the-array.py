from math import ceil
class Solution:
    def isPalindrome(self, word: str) -> bool:
        print(word[:len(word)//2] , word[ceil(len(word)/2):])
        return word[:len(word)//2] == word[ceil(len(word)/2):][::-1]
    
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        
        return ''