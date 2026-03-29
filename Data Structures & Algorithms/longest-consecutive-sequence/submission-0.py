class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        no_dupes = set(nums)
        max = 0
        for num in nums:
            if (num-1) not in no_dupes:
                length = 0 
                while(num+length)in no_dupes:
                    length+=1
                if length > max:
                    max = length
        return max



        