class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.minStack) == 0 or self.minStack[-1] >= val:
            self.minStack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            num = self.stack.pop()
            if num == self.minStack[-1]:
                self.minStack.pop()
        else:
            return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
