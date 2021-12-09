from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.d.get(key)!=None:
            n = self.d[key]
            self.d.move_to_end(key,last=False)
            return n 
        return -1
    def put(self, key: int, value: int) -> None:
        if self.d.get(key)!=None:
            self.d[key] = value
            self.d.move_to_end(key,last=False)
        else:
            if len(self.d.keys()) >= self.capacity:
                self.d.popitem()
            self.d[key]=value
            self.d.move_to_end(key,last=False)
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

