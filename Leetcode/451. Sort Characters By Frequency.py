class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        res = []
        list1 = sorted([(count[i], i) for i in count], reverse= True)
        for a, b in list1:
            res.append(b * a)
        return ''.join(res)
