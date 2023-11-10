class StockSpanner:

    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        day = 1
        while self.stack and self.stack[-1][0] <= price:
            day += self.stack.pop()[1]
        self.stack.append((price, day))
        return day
