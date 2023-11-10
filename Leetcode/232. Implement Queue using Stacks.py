class MyQueue:
    def __init__(self):
        self.A, self.B = [], []
    def push(self, x):
        self.A.append(x)
    def pop(self):
        self.rearrange()
        return self.B.pop(-1)
    def peek(self):
        self.rearrange()
        return self.B[-1]
    def empty(self):
        return (len(self.A) + len(self.B)) == 0
    def rearrange(self):
        if len(self.B) == 0:
            while self.A:
                self.B.append(self.A.pop(-1))