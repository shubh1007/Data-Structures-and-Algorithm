class MyStack:

    def __init__(self):
        self.Q = []        

    def push(self, x: int) -> None:
        self.Q.append(x)

    def pop(self) -> int:
        if self.empty(): return None
        return self.Q.pop(-1)

    def top(self) -> int:
        if self.empty(): return None
        return self.Q[-1]

    def empty(self) -> bool:
        return len(self.Q) == 0
            