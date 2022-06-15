class Solution:
    def calculate(self, s: str) -> int:
        
        stk = []
        total = 0
        open_brackets = 0
        N= len(s)
        i=0
        while i < N:
            chr = s[i]
            if '(' == chr:
                open_brackets+=1
                stk.append(chr)
                i+=1
            elif ')' == chr:
                if open_brackets<1 or stk[-1] == '-' or stk[-1] == '+':
                    return None
                tmp = []
                last_num = None
                while stk[-1] != '(':
                    curr = stk.pop()
                    # tmp.insert(0, curr)
                    if curr == '-':
                        tmp.append(-last_num)
                        last_num = None
                        
                    elif curr == '+':
                        tmp.append(last_num)
                        last_num = None
                        
                    else:
                        last_num = int(curr)
                if last_num:
                    tmp.append(last_num)
                stk.pop()
                total = sum(tmp)
                stk.append(total)
                open_brackets-=1
                # if len(tmp)>0 and tmp[0] == '-':
                #     tmp.insert()
                i+=1
            elif chr in ['+', '-']:
                stk.append(chr)
                i+=1
            elif ' ' != chr:
                    tmp_num = []
                    while i < N and s[i] not in ['-','+','(',')',' ']:
                        # prin
                        tmp_num.append(s[i])
                        i+=1
                    # print(i,tmp_num)
                    stk.append(''.join(tmp_num))
            else:
                i+=1
        # print(stk)  
        if len(stk) > 0:
            last_num = None
            tmp = []
            
            while stk:
                
                curr = stk.pop()
                if curr == '-':
                    tmp.append(-last_num)
                    last_num = None
                elif curr == '+':
                    tmp.append(last_num)
                    last_num = None
                    
                else:
                    last_num = int(curr)
            if last_num:
                tmp.append(last_num)
            print(tmp)
            return sum(tmp)

                
        