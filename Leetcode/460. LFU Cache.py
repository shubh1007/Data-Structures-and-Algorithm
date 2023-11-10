class ListNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = self.next = None

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        
    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)