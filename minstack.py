class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.mini == []:
            self.mini.append(value)
        else:
            self.mini.append(min(self.mini[-1], value))

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()