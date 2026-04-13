class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n * 2
        # closing parentheses must always be less than or equal open
        # a counter for the op and counter for the close
        res = []
        def traverse(op, close, curr, n):
            if len(curr) == n*2:
                res.append(curr)
                return
            if op < n:
                traverse(op+1, close, curr+"(", n)
            if close < op:
                traverse(op, close+1, curr+")", n)
        traverse(0, 0, "", n)
        return res                

        