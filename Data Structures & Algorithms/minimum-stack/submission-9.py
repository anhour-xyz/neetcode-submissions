class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
