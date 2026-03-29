class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        l = 0 #left
        max_frequency = 0
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1
            max_frequency = max(max_frequency, count[s[i]])
            if i-l+1 - max_frequency > k:
                count[s[l]] -= 1
                l+=1
            max_length = max( max_length, i-l+1)
        return max_length
            
            
            
        
        