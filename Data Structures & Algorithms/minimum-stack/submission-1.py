class MinStack:

    def __init__(self):
        self.stack = []
        self.getBottom = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.getBottom:
            self.getBottom.append(val)
        else:
            self.getBottom.append(min(val, self.getBottom[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.getBottom.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.getBottom[-1]