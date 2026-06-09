class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maps = {}
        length = 0
        for r in range(len(s)):
            if s[r] in maps:
                l = max(l, maps[s[r]]+1)
            maps[s[r]] = r
            length = max(length, r-l+1)
        return length