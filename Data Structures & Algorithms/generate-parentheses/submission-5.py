class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []

        def backTracking(openN: int = 0, closedN: int = 0) -> None:
            if closedN == openN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backTracking(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backTracking(openN, closedN+1)
                stack.pop()

        backTracking()

        return res