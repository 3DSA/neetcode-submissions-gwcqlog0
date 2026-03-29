class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        og = set(nums)
        max = 0
        for num in nums:
            if (num-1) not in og:
                length = 0
                while (num+length) in og:
                    length +=1
                if length > max:
                    max = length
        return max