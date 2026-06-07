class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        for num in nums:
            maps[num] = maps.get(num,0) + 1
        arr = []
        for key,val in maps.items():
            arr.append([val, key])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        