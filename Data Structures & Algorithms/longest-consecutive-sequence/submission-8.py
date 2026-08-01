class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seq = 0
        for num in nums:
            if num-1 not in nums:
                total = 1
                while num+1 in nums:
                    num += 1
                    total +=1
                
                seq = max(seq,total)
        return seq
        