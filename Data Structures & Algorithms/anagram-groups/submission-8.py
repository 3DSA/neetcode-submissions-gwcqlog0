class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for word in strs:
            count = [0]*26
            for s in word:
                count[ord(s)-97] += 1
            maps.setdefault(tuple(count), []).append(word)
        
        res = []
        for _, groups in maps.items():
            res.append(groups)
        return res
        