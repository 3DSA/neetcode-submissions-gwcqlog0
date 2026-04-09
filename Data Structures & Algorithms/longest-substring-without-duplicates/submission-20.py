class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        maps = {}
        l = 0
        for r in range(len(s)):
            if s[r] in maps:
                if maps[s[r]]+1 > l:
                    l = maps[s[r]]+1
                maps[s[r]] = r
            else:
                maps[s[r]] = r
            max_length = max(max_length, r-l+1)
        return max_length
                