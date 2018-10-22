class Solution(object):
    def countC(self,c,numstr,start):
        endstr = len(numstr)
        i = start
        while i < endstr:
            if numstr[i]!=c:
                break
            i+=1
        return i-start
    def saynN(self,numstr):
        idx = 0
        tmp = ""
        while idx < len(numstr):
            #print c
            c = numstr[idx]
            cnt = self.countC(c,numstr,idx)
            tmp +=str(cnt)+c
            idx+=cnt
        return tmp
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        numstr = "1"
        for i in range(2,n+1):
            numstr = self.saynN(numstr)
            #print i,numstr
        return numstr
sol = Solution()
test_data = [3,4,5]
for d in test_data:
    print sol.countAndSay(d)
