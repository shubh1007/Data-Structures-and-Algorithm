def HCF(x, y):
    res = 1
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i ==0:
            res = i
    return res

print(HCF(70, 15))