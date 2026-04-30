class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) +1
        
        arr = []
        for key,item in count.items():
            arr.append([item, key])
        
        arr.sort()

        res = []
        while  len(res) < k:
            curr = arr.pop()
            res.append(curr[1])

        return res
        