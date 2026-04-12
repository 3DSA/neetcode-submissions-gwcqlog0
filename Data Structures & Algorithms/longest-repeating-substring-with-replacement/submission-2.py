class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_length = 0
        curr = None
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if not curr or count[curr] < count[s[r]]:
                curr = s[r]
            if count[curr] +k < r-l+1:
                count[s[l]] -= 1
                l+= 1
            max_length = max(max_length, r-l+1)
        return max_length
        
        