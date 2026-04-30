class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for word in strs:
            count = [0]*26
            for s in word:
                count[ord(s)-97] += 1
            count = tuple(count)
            maps.setdefault(count, []).append(word)
        
        res = []
        for key, arr in maps.items():
            res.append(list(arr))
        return res
        