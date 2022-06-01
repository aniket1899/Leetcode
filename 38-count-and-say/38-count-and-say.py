class Solution:
    def generate_say(self, say, iter ,n):
        if iter == n:
            return say
        else:
            
            result = ""
            i = 0
            while i < len(say):
                cnt = 1
                ch = say[i]
                i+=1
                while i < len(say) and ch == say[i]:
                    cnt +=1
                    i+=1
                # if iter ==5:
                #     print((str(cnt) , ch))
                result += str(cnt) + ch
                
                
        
            return self.generate_say(result, iter+1 ,n)
            
                
            
            
    def countAndSay(self, n: int) -> str:
        
        return self.generate_say("1", 1 ,n)
        