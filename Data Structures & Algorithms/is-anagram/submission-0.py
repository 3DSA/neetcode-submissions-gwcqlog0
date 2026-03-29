class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr_s = [0] * 26
        arr_t = [0] * 26
        for i in range(len(s)):
            arr_s[ord(s[i])-97] += 1
            arr_t[ord(t[i])-97] += 1
        if arr_s == arr_t:
            return True
        return False
