class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        validMap = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        for char in s:
            if char in validMap:
                if stack and stack[-1] == validMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack