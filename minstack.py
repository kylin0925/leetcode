class MinStack(object):
    elem = []
    minq = []
    cnt = 0
    top = 0
    minNum = 0
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elem = []
        self.minq = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.elem) == 0:
            self.minNum = x
            
        else:
            if self.minNum > x:
                self.minNum =x
                
        self.minq.append(self.minNum)        
        self.elem.append(x)
        #print "after push"
        #print self.minq
        #print self.elem
    def pop(self):
        """
        :rtype: void
        """
        self.minq.pop()        
        r = self.elem.pop()
        if len(self.minq) > 0:
            self.minNum = self.minq[-1]
        #print "after pop"
        #print self.minq
        #print self.elem
        return r
    def top(self):
        """
        :rtype: int
        """
        return self.elem[-1]

    def getMin(self):
        """
        :rtype: int
        """               
        return self.minq[-1]        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


minStack = MinStack();
'''
minStack.push(2147483646);
minStack.push(2147483646);
minStack.push(2147483647);
print minStack.top();
minStack.pop()
print minStack.getMin();  
minStack.pop();
print minStack.getMin();  
minStack.pop();
minStack.push(2147483647);
print minStack.top();
print minStack.getMin();  
minStack.push(-2147483648);
print minStack.top();


'''
minStack.push(-10)
minStack.push(14)
print minStack.getMin()
print minStack.getMin()
minStack.push(-20)
print minStack.getMin()
print minStack.getMin()
print minStack.top()
print minStack.getMin()
minStack.pop()
minStack.push(10)
minStack.push(-7)
print minStack.getMin()
minStack.push(-1)
minStack.pop()
print minStack.top()
print minStack.getMin()
minStack.pop()
#[[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]
