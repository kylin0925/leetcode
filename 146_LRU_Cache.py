from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.q = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.hashmap.get(key) == None:
            #print("get",key,"Not found",self.q)
            return -1
        n = self.hashmap.get(key)
        if n ==-1:
            return n
        self.q.remove(key)
        self.q.appendleft(key)
        #print("get",key,self.q)
        return n
    def put(self, key: int, value: int) -> None:
        if self.hashmap.get(key)!=None and self.hashmap.get(key)!=-1:
            
            self.hashmap[key]=value
            self.q.remove(key)
            self.q.appendleft(key)
            
        else:
            if len(self.hashmap.keys()) >= self.capacity:
                #print("test")
                n = self.q.pop()
                self.hashmap[n]=-1
            self.q.appendleft(key)
            self.hashmap[key]=value;
            
        #print("put",key,self.q,self.hashmap)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

