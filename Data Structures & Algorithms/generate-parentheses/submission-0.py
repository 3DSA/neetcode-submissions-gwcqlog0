class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = set()

        def parenthesis(count=0, op=0, cl=0, s=""):
            if count == n*2:
                res.add(s)
                return
            if op < n:
                parenthesis(count+1, op+1, cl, s+"(")
            if cl < op:
                parenthesis(count+1, op, cl+1, s+")")
        parenthesis()
        return list(res)
            
        