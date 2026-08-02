class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop()+stack.pop())
            elif token == "-":
                left = stack.pop()
                right = stack.pop()
                stack.append(right-left)
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                left = stack.pop()
                right = stack.pop()
                stack.append(int(right/left))
            else:
                stack.append(int(token))
        return stack.pop()