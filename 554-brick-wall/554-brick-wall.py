class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # added = []
        count = {}
        
        for w in wall:
            # tmp = []
            x = 0
            
            for e in w[:-1]:
                x = x + e
                # tmp.append(x)
                if x in count.keys():
                    count[x] += 1
                else:
                    count[x] = 1
                # x = e
            # added.append(tmp)
        # print(count)
        # count[x] = 0
        # print(max(count.values()))
        if len(count.values()) == 0:
            return len(wall)
        return len(wall) - max(count.values())
            
        
        
        