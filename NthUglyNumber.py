class DLL:
    def __init__(self, val = 0):
        self.val = val
        self.prev = None
        self.next = None

    def insert(self, tail, val):
        if tail.val == val: return tail
        elif tail.val < val:
            temp = DLL(val)
            temp.prev = tail
            tail.next = temp
            tail = temp
            return tail
        else:
            temp = tail
            while temp and temp.val > val:
                temp = temp.prev
                
            if temp and temp.val == val:
                return tail
            else:
                newNode = DLL(val)
                newNode.next = temp.next
                temp.next = newNode
                newNode.prev = temp
                newNode.next.prev = newNode
                return tail

class SLL:
    def __init__(self, val = 0):
        self.val = val
        self.next = next
    
    def count(self, root):
        temp = root
        c = 0
        while temp: 
            temp = temp.next
            c += 1
        return c
        
            
dllHead = DLL(1)
dllTail = dllHead
sllHead = None
count = 0
n = 398
while count != n:
    value = dllHead.val
    two = value * 2
    three = value * 3
    five = value * 5
    
    dllTail = dllHead.insert(dllTail, two)
    dllTail = dllHead.insert(dllTail, three)
    dllTail = dllHead.insert(dllTail, five)
    
    temp = SLL(dllHead.val)
    temp.next = sllHead
    sllHead = temp
    
    dllHead = dllHead.next
    dllHead.prev = None
    
    count = sllHead.count(sllHead)
    
print(sllHead.val)









