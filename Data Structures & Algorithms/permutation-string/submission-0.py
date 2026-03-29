class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for char in s1:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
        string_c = {}
        window = len(s1)-1
        l = 0
        for r in range(len(s2)):
            if s2[r] not in string_c:
                string_c[s2[r]] = 1
            else:
                string_c[s2[r]] += 1
            if r-l > window:
                string_c[s2[l]] -=1
                if string_c[s2[l]] == 0:
                    string_c.pop(s2[l])
                l +=1
            print(string_c)
            if count == string_c:
                return True
        return False
        
