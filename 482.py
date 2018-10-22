class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """ 
        slist = S.split('-')
        slist = "".join(slist)
        slist = [c for c in slist]
        
        r = len(slist) % K
        
        tmp = ""
        res = ""
        if r > 0:
            tmp = "".join(slist[0:r])
            
   
        if tmp!="":
            res = tmp+"-"
        for i in range(len(tmp),len(slist),K):
            
            t = slist[i:i+K]
            #print "".join(t)
            res+= "".join(t) + "-"
        return res[0:-1].upper()
        
        
sol = Solution()
test_data = [["5F3Z-2e-9-w",4],[ "2-5g-3-J", 2],["abcdefghijk",5],["a",3],["a",1] ]
for d in test_data:
    print sol.licenseKeyFormatting(d[0],d[1])
