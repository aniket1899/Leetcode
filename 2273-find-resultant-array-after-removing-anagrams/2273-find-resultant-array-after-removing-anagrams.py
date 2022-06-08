class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # wordsSorted = [(sorted(word), 0) for word in words]
        # wordsDict = {w:0 for set(wordsSorted)}
        
        # print(wordsSorted)
#         words_count={}
#         # print(words)
#         for i, word in enumerate(words):
            
#             tmp = ''.join(sorted(word))
#             # print(tmp)
#             if  tmp not in words_count.keys():
#                 words_count[tmp] = i
                
#         unique = []
#         for w in words_count.values():
#             unique.append(words[w])
            
        
#         return unique
        results = []
        last = None
        for word in words:
            tmp =sorted(word)
            if last != tmp:
                results.append(word)
            last = tmp
            
        return results
                
        