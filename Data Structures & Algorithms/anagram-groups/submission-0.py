class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for word in strs:
            freqs = [0]*26
            for ltr in word:
                freqs[ord(ltr)-97] +=1
            freq = tuple(freqs)
            if freq in maps:
                maps[freq].append(word)
            else:
                maps[freq] = [word]
        return list(maps.values())