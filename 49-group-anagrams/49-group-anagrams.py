class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        combinations = []
        
        strs_sorted = [(''.join(sorted(s)), s) for s in strs]
        strs_dict = {k[0]:[] for k in set(strs_sorted)}
        
        for s_key, s in strs_sorted:
            strs_dict[s_key].append(s)
            
        return list(strs_dict.values())
            
        
        
        
        
        # strs_sorted = [(''.join(sorted(s)), i) for i, s in enumerate(strs)]
        # strs_sorted.sort()
        # print(strs)
        # N = len(strs)
        # i = 0
        # while i < N:
        #     tempss = strs_sorted[i]
        #     temp_res = [strs[tempss[1]]]
        #     i+=1
        #     while i < N and tempss[0] == strs_sorted[i][0]:
        #         temp_res.append(strs[strs_sorted[i][1]])
        #         i += 1
        #     combinations.append(temp_res)
            
        
        # for st, st_sorted in zip(strs, strs_sorted)
        
        # combinations = []
        # visited = []
        # com_index_in_visited = []
        # for s in strs:
        #     s_copy = s
        #     s = sorted(s)
        #     if s in visited:
        #         idx = visited.index(s)
        #         combinations[com_index_in_visited[idx]].append(s_copy)
        #     else:
        #         visited.append(s)
        #         com_index_in_visited.append(len(combinations))
        #         combinations.append([s_copy])
        
        # return combinations
        