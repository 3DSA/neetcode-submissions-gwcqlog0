class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for num in nums:
            maps[num] = maps.get(num, 0) + 1
        print(maps)
        arr = []
        for num in maps:
            arr.append([maps[num], num]) # count, num
        arr.sort()
        print(arr)
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

            