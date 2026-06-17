class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for s in s1:
            count[s] = count.get(s,0) + 1
        
        l = 0
        curr = {}
        for r in range(len(s2)):
            curr[s2[r]] = curr.get(s2[r],0) + 1
            if r-l+1 > len(s1):
                curr[s2[l]] -= 1
                if curr[s2[l]] == 0:
                    curr.pop(s2[l])
                l += 1
            if curr == count:
                return True
        return False
        