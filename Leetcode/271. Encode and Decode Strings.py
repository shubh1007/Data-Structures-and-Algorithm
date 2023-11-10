class Solution:
    def encode(self, strs):
        res = ""
        for string in strs:
            res += len(string) + "/" + string
        return res

    def decode(self, str_):
        res = []
        i = 0
        while i < len(str_):
            temp = i
            while temp < len(str_) and str_[temp] != "/":
                temp += 1
            size = int(str_[i: temp])
            word = str_[temp + 1: temp + 1 + size]
            i = temp + 1 + size 
            res.append(word)
        return word


