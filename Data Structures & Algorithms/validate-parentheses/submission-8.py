class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for chrs in s:
            if chrs == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif chrs == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif chrs == "]":
                if not stack or stack.pop() != "[":
                    return False
            else:
                stack.append(chrs)
        if not stack:
            return True
        return False
