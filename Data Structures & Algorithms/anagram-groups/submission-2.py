class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for word in strs:
            freqs = [0]*26
            for i in word:
                i = i.upper()
                freqs[ord(i)-65] += 1
            freqs = tuple(freqs)
            if freqs not in count:
                count[freqs] = [word]
            else:
                count[freqs].append(word)
        res = []
        for i in count:
            res.append(count[i])
        return res