class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        # for i in range(len(self.pages) - self.curr):
        #     self.pages.pop(-1)
        #     self.curr -= 1
        self.pages = self.pages[:self.curr + 1] + [url]
        # self.pages.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)    
        return self.pages[self.curr]

    def forward(self, steps: int) -> str:
        if (self.curr + steps) >= len(self.pages):
            self.curr = len(self.pages) - 1
        else:
            while steps:
                self.curr += 1
                steps -= 1
        return self.pages[self.curr]


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)