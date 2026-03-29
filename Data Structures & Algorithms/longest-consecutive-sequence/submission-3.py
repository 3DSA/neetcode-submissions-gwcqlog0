class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashes = set(nums)
        starters = []
        for num in nums:
            if num-1 not in hashes:
                starters.append(num)
        longest = 0 
        for start in starters:
            long = 0
            while start in hashes:
                long +=1
                start +=1
            if long > longest:
                longest = long
            
        return longest

        