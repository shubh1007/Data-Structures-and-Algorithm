class DisjointSet:
    def __init__(self, n) -> None:
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return x
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        elif self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            self.rank[yRoot] += 1

n = 10
ds = DisjointSet(n)
ds.union(0, 1)
ds.find(0)
ds.find(1)
print(ds.parent)