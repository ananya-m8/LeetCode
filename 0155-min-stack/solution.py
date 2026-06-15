class MinStack:

    def __init__(self):
        self.stack=[]
        self.mine=[]
    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.mine:
            value=min(self.mine[-1],value)
        self.mine.append(value)
    def pop(self) -> None:
        self.stack.pop()
        self.mine.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mine[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
