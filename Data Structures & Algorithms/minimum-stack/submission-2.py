class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_value = float("inf")
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_value:
            self.min_value = val
        
        self.min_stack.append(self.min_value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.min_value = self.min_stack[-1] if self.min_stack else float('inf')
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
