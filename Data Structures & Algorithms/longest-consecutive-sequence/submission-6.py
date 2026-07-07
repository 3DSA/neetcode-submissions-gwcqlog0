class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        length = 0
        for element in elements:
            if element-1 not in elements:
                curr = 1
                while element+1 in elements:
                    element += 1
                    curr +=1
                length = max(length,curr)
        return length
        