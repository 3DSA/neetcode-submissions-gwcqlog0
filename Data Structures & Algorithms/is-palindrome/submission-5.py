class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        backwards = ""
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                backwards += s[i]
        if backwards == backwards[::-1]:
            return True
        return False
        
        