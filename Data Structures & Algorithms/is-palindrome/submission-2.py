class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        sent = [char for char in s if char.isalnum()]
        left = 0
        right = len(sent)-1
        while left < right:
            if sent[left] != sent[right]:
                return False
            left +=1
            right -=1
        return True
