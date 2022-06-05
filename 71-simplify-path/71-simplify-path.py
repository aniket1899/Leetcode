class Solution:
    def simplifyPath(self, path: str) -> str:
        path_sep = path.split('/')
        i=0
        print(path_sep)  
        cano = []
        
        for p in path_sep:
            if len(p) >0:
                if '..' == p:
                    try:
                        cano.pop()
                    except:
                        continue
                elif '.' != p:
                    cano.append(p)
            
            
            
            # if len(path_sep[i]) > 0:
            #     if '..' == path_sep[i]:
            #         path_sep.pop(i)
            #         i-=1
            #         if i>0:
            #             path_sep.pop(i-1)
            #             i-=1
            #     elif '.' == path_sep[i]:
            #         path_sep.pop(i)
            #         i-=1
            # else:
            #     path_sep.pop(i)
            #     i-=1
            # i+=1
                    
        # print(cano)  
        return '/'+'/'.join(cano)
        