class Solution:
    def isValid(self, s: str) -> bool:
         # bracket_count = {'round': 0, 'curly': 0, 'square': 0}
        latest = [] #last opened bracket
        
        for  e in s:
            # print(e)
            if e == '(':
                # bracket_count['round'] +=1
                latest.append('round')
            elif e == '{':
                # bracket_count['curly'] +=1
                latest.append('curly')
            elif e == '[':
                # bracket_count['square'] +=1
                latest.append('square')
                
            else:
                
                if len(latest) == 0:
                    # print(e)
                    return False
                else:
                    if e == ')' and latest[-1] == 'round':
                        # bracket_count['round'] -=1
                        latest.pop()
                        
                    elif e == '}' and latest[-1] == 'curly':
                        # bracket_count['curly'] -=1
                        latest.pop()
                    elif e == ']' and latest[-1] == 'square':
                        # bracket_count['square'] -=1
                        latest.pop()
                    else:
                        return False
                    
        # if sum(bracket_count.values()) == 0:
        if len(latest) == 0:

            return True
        else:
            return False
                    