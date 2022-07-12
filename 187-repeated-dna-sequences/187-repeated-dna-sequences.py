from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # s = 'x' + s
        # dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s))]
        # seq10 = set([])
        # for top in range(1, len(s)):
        #     for bot in range(len(s)):
        #         if s[top] == s[bot] and top != bot:
        #             dp[top][bot] = dp[top-1][bot-1] + 1
        #             if dp[top][bot] >= 10:
        #                 tmp = ''
        #                 i = top
        #                 for _ in range(10):
        #                     tmp = s[i] + tmp
        #                     i -= 1
        #                 seq10.add(tmp)
        # # for i in range(len(s)):
        # #     print(dp[i])
        # return list(seq10)
        ctr = defaultdict(int)
        valid_subseqs = set([])
        for i in range(len(s)-9):
            # print(i, len(s))
            subseq  = s[i:i+10]
            if ctr[subseq] == 0:
                ctr[subseq] = 1
            else:
                valid_subseqs.add(subseq)
            # if ctr[subseq] <= 1:
            #     ctr[subseq] += 1
            #     if ctr[subseq] > 1:
            #         valid_subseqs.add(subseq)
        # print(ctr)
        return list(valid_subseqs)
                        
        