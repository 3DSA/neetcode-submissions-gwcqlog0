class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        checks = []
        max_length = 0
        for num in count:
            if not (num-1) in count:
                checks.append(num)

        for num in checks:
            l = 0
            while num in nums:
                l +=1
                num +=1
            max_length = max(max_length, l)
        return max_length
        