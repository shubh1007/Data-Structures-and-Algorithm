class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.front = self.rear = -1
        self.queue = [0] * k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if (self.front == -1):
            self.front = self.rear = 0
            self.queue[self.front] = value
        elif (self.rear + 1) % self.size == self.front:
            return False
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.front == -1: return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.front == -1: return -1
        else: return self.queue[self.front]
        
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.rear == -1: return -1
        else: return self.queue[self.rear]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return True if self.front == -1 else False

    def isFull(self):
        """
        :rtype: bool
        """
        return ((self.rear + 1) % self.size == self.front)
            
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
