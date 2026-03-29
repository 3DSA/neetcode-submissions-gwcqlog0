class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a map to get repeating chars and index, then update index
        # use left pointer to move index to that
        maps = {}
        l = 0
        max_length = 0
        for r in range(len(s)):
            if s[r] in maps:
                l = max(l,maps[s[r]]+1)
            max_length = max(max_length, r-l+1)
            maps[s[r]] = r
        return max_length

