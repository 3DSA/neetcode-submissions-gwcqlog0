class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ""
        s = s.lower()
        for chars in s:
            if chars.isalnum():
                sentence += chars
        
        sentence.lower()
        return sentence == sentence[::-1]