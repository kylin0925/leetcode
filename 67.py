class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        reva = a[::-1]
        revb = b[::-1]
        #print reva,revb
        len_a = len(a)
        len_b = len(b)
        idx = 0
        add_len = min(len_a,len_b)
        c = 0
        res = ""
        #print len_a,len_b,add_len
        while idx < add_len:
            #print "idx",idx
            tmpa = int(reva[idx])
            tmpb = int(revb[idx])
            r = (tmpa+tmpb + c)%2
            c = (tmpa+tmpb + c)/2
            #print "r",r,"c",c
            res +=str(r)
            idx+=1
        #print "res",res
        if len_a > len_b:
            while idx < len_a:
                #print "idx",idx
                tmpa = int(reva[idx])
                #print "tmpa",tmpa
                r = (tmpa+ c)%2
                c = (tmpa+ c)/2
                res +=str(r)
                idx+=1                      
        if len_b > len_a:
            while idx < len_b:
                #print "idx",idx
                tmpb = int(revb[idx])
                #print "tmpa",tmpb
                r = (tmpb+ c)%2
                c = (tmpb+ c)/2
                res +=str(r)
                idx+=1          
        if c > 0:
            res+=str(c)
        #print res[::-1]
        return res[::-1]
sol = Solution()
test_data = [ ["11", "1"] ,["1010", "1011"],["1", "11"],["1", "1"],["1", "0"],["0", "0"]]
for d in test_data:
    print sol.addBinary(d[0],d[1])
