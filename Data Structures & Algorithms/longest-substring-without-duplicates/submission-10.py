class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}  # HashMap to store the last index of each character
        l = 0  # Left pointer of the sliding window
        res = 0  # Stores the length of the longest substring

        for r in range(len(s)):  # Right pointer moves through the string
            if s[r] in mp:  
                # If character s[r] is already in the map, move left pointer (l)
                # We move l to the right of the last seen index of s[r]
                l = max(mp[s[r]] + 1, l)  
            
            # Update the last index of s[r] in the hashmap
            mp[s[r]] = r
            
            # Update the result with the length of the current substring
            res = max(res, r - l + 1)
        
        return res