class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []

        def backtracking(openN: int = 0, closedN: int = 0) -> None:
            if closedN == openN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtracking(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtracking(openN, closedN+1)
                stack.pop()

        backtracking()

        return res