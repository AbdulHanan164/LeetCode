class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Python's '/' operator performs floor division for integers
                    if a * b < 0 and a % b != 0:
                        stack.append(a // b + 1)
                    else:
                        stack.append(a // b)
            else:
                stack.append(int(token))
        
        return stack[0]
