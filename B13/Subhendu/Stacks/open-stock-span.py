class StockSpanner:
    ### https://leetcode.com/problems/online-stock-span/

    def __init__(self):
        self.stack = []
        self.idx = 0

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if self.stack:
            span = self.idx - self.stack[-1][1] + 1
        self.idx += 1
        self.stack.append((price, self.idx))
        return span