class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return True

        stack = []
        closedToOpen = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        for c in s:
            if c in closedToOpen.keys():
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack