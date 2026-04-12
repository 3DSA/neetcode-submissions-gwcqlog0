class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length  = 0
        count = {}
        l = 0
        for r in range(len(s)):
            if s[r] in count:
                l = max(l, count[s[r]]+1)
            count[s[r]] = r
            max_length = max(max_length, r-l+1)
        return max_length