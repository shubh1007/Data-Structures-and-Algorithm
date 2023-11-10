array = [1, 4, 5]
result = []
for i in range(max(array)):
    string = ""
    for j in range(len(array)):        
        if array[j] > 0: string += "* "
        else: string += "  "
        array[j] -= 1
    result.append(string)

for i in range(len(result)-1, -1, -1):
    print(result[i])
    
    
    
    
    









