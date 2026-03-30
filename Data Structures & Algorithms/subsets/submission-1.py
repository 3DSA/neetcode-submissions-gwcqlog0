class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        for i in nums:
            length = len(arr)
            for j in range(length):
                add = arr[j].copy()
                add.append(i)
                arr.append(add)
        return arr
