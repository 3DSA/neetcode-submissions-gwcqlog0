class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for word in strs:
            arr = [0] * 26
            for s in word:
                arr[ord(s)-97] += 1
            maps.setdefault(tuple(arr),[]).append(word)

        res = []
        for _,items in maps.items():
            res.append(items)
        return res
    