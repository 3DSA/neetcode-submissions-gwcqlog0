class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for word in strs:
            count = [0] * 26
            word = word.lower()
            for s in word:
                count[ord(s)-97] += 1
            maps.setdefault(tuple(count), []).append(word)
        
        arr = []
        for _, pairs in maps.items():
            arr.append(pairs)
        return arr
        