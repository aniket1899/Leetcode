class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        fringe = []
        
        for i, c in enumerate(candidates):
            fringe.append(([c], i))  # ([list of candidates], current index pointing to candidates)
        
        results = []
        N = len(candidates)
        while fringe:
            variables, idx = fringe.pop(0)
            
            
            if sum(variables) == target:
                results.append(variables)
                
            elif sum(variables) < target and idx < N:
                # tmp_vars = []
                for i in range(idx, N):
                    tmp_vars = variables+[candidates[i]]
                    # if i == idx:
                    #     fringe.append((tmp_vars, idx))
                    # else:
                    fringe.append((tmp_vars, i))
            
            
        return results
                    