class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for char in tokens:
            print(stack)
            if char == "+":
                a = stack.pop()
                b = stack.pop()
                res = b + a
                stack.append(res)
            elif char == "-":
                a = stack.pop()
                b = stack.pop()
                res = b - a
                stack.append(res)
            elif char == "*":
                a = stack.pop()
                b = stack.pop()
                res = b * a
                stack.append(res)
            elif char == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(char))

        print(stack)
        return stack[0]