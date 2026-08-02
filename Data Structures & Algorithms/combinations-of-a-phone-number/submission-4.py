class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        book ={
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
        def bfs(i, curr):
            if i == len(digits):
                res.append(curr.copy())
                return
            
            for s in book[digits[i]]:
                curr.append(s)
                bfs(i+1,curr)
                curr.pop()
        
        bfs(0,[])
        groups = []
        for group in res:
            groups.append("".join(group))
        return groups
        