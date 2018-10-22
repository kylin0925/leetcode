class Solution(object):
    binwatch = [0,0,0,0,0,0,0,0,0,0,0]
    res = []
    def dfs(self,idx,n,target):
        #print idx
        if n == target:
            h = [str(b) for b in self.binwatch[0:4]]
            m = [str(b) for b in self.binwatch[4:]]
            h = "0b"+"".join(h)
            m = "0b"+"".join(m)
            ih = int(h,2)
            im = int(m,2)
            #print ih,im
            if ih < 12 and im < 60:
                #print "%d:%02d" % (ih,im)
                self.res.append("%d:%02d" % (ih,im))
            return
        for i in range(idx+1,11):
            self.binwatch[i] = 1
            self.dfs(i,n+1,target)
            self.binwatch[i] = 0
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.res = []
        self.dfs(-1,0,num) 
        return self.res
sol = Solution()
test_data = [ 2]
for d in test_data:
    print sol.readBinaryWatch(d)
