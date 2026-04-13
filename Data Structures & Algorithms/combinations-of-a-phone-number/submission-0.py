class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        maps = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def calc(i, curr=""):
            nonlocal digits
            if not digits or i > len(digits)-1:
                print(curr)
                res.append(curr)
                return
            for chars in maps[digits[i]]: # char would a in abc
                calc(i+1, curr+chars)
        calc(0)
        return res

        