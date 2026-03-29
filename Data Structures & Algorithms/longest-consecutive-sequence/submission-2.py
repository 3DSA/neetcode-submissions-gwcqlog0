class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        starters = []
        for num in nums:
            if (num-1) not in unique:
                starters.append(num)
        max_top = 0
        print(starters)
        for start in starters:
            num = start
            top = 0
            while num in unique:
                top +=1
                num+=1
            if top > max_top:
                max_top = top
        return max_top
        