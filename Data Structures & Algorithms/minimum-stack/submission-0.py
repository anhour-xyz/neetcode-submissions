class MinStack:

    def __init__(self):
        self.stack = []
        self.getTop = []
        self.getBottom = []
        self.up = float('-inf')
        self.bottom = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.up = max(self.up, val)
        self.bottom = min(self.bottom, val)
        self.getTop.append(self.up)
        self.getBottom.append(self.bottom)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.getTop[-1]: self.getTop.pop()
        if num == self.getBottom[-1]: self.getBottom.pop()
        
    def top(self) -> int:
        
        return self.getTop[-1]

    def getMin(self) -> int:
        
        return self.getBottom[-1]
