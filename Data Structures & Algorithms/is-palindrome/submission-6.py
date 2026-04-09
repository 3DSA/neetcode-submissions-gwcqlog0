class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        s = s.lower()
        for chars in s:
            if chars.isalnum():
                filtered += chars
        return filtered == filtered[::-1]
        