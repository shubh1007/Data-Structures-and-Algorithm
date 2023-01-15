class DisjointSet:
    def __init__(self, n) -> None:
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x: int) -> int:
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        # print(self.parent)
        return x
    
    def union(self, x: int, y: int) -> None:
        xRoot = self.find(x)
        yRoot = self.find(y)
        # print(f"Union of x = {xRoot}\nUnion of y = {yRoot}")
        if xRoot == yRoot:
            return
        elif self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[yRoot] += 1

n = 10
ds = DisjointSet(n)
# print(ds.find(3))
ds.union(0, 1)
print(ds.find(0))
print(ds.find(1))




        