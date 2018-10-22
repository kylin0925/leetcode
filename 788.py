class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def isMagic(n):
            lstn = [int(i) for i in str(n) ]
            #print "isMagic lstn",lstn
            for i in range(len(lstn)):
                if lstn[i] == 3 or lstn[i] == 4 or lstn[i] == 7: 
                    return 0
                if lstn[i] == 2:
                    lstn[i] = 5
                elif lstn[i] == 5:
                    lstn[i] = 2                    
                elif lstn[i] == 6:
                    lstn[i] = 9
                elif lstn[i] == 9:
                    lstn[i] = 6
                
                   
            
            tmp = ""
            
            for i in lstn:
                tmp +=str(i)
           
            return int(tmp)!=n
        cnt = 0        
        for i in xrange(1,N+1):            
            cnt += isMagic(i)
        return cnt    
sol = Solution()
test_data = [857]
for d in test_data:
    print sol.rotatedDigits(d)
