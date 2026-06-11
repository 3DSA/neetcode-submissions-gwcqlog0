class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        def merge(left, right):
            res = ""
            counter = 0
            while left and right:
                if counter % 2 == 0:
                    res += left.pop(0)
                else:
                    res += right.pop(0)
                counter +=1
            while left:
                res += left.pop(0)
            while right:
                res+= right.pop(0)
            return res
        return merge(word1, word2)
        