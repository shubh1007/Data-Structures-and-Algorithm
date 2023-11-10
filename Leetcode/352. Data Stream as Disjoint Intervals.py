class SummaryRanges:
    def __init__(self) -> None:
        self.set = set()
    def addNum(self, value: int) -> None:
        self.set.add(value)
    def getIntervals(self) -> list[list[int]]:
        res = []
        index = 1
        arr = sorted(list(self.set))
        start = arr[0]
        curr = arr[0]
        if len(arr) == 1:
            res.append([start, start])
            return res
        while index < len(arr):
            if arr[index] != curr + 1:
                res.append([start, arr[index - 1]])
                start = arr[index]
            curr = arr[index]
            index += 1
        res.append([start, arr[index - 1]])
        return res