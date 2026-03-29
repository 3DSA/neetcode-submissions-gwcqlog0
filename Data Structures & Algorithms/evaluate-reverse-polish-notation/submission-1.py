class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                stack.append(-(stack.pop() - stack.pop()))
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "/":
                var1 = stack.pop()
                var2 = stack.pop()
                stack.append(int(float(var2 / var1)))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()


        