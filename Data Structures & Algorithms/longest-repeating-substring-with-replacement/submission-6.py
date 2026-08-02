class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maps = {}
        l = 0
        length = 0
        for r in range(len(s)):
            maps[s[r]] = maps.get(s[r],0) + 1
            if (r-l+ 1) - maps[s[l]] > k:
                maps[s[l]] -= 1
                l+= 1
            length = max(length, min(maps[s[r]] + k, len(s)))
        return length
        