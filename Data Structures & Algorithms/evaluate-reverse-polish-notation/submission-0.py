class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # The first popped element is the right operand (b)
                # The second popped element is the left operand (a)
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # int() division in Python naturally truncates toward zero
                    stack.append(int(a / b))
            else:
                # Token is a number, push it to the stack
                stack.append(int(token))
                
        return stack[0]

        