class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maps = {}
        l = 0
        length = 0
        for r in range(len(s)):
            if s[r] in maps:
                l = max(maps[s[r]]+1, l)
            maps[s[r]] = r
            length = max(length, r-l+1)
        return length
        