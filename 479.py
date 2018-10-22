class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [ 0,9,9009,906609 , 99000099, 9966006699,  999000000999,99956644665999,  9999000000009999]
        return table[n]%1337

'''        
def chkPalindrome(firsthalf,maxbehave,ml):
    while firsthalf > 0:
        i = 0
        while i < maxbehave:
            tmp = str(firsthalf*ml+i)
            rhtmp = tmp[len(tmp)/2:]
            rhtmp = rhtmp[::-1]
            if tmp[0:len(tmp)/2] ==rhtmp:
                print tmp,firsthalf,i
                return
            i+=1
        firsthalf-=1
'''
def chkPalindrome(p):
    
    rhtmp = p[len(p)/2:]
    rhtmp = rhtmp[::-1]
    if p[0:len(p)/2] ==rhtmp:
        return True;
def reverse(n):
    tmp = str(n)[::-1]
    return int(tmp)
def buildTable():
    for n in range(2,9,):
        p = 10**n-1
        ml = 10**n
        #print (10**n-1) - ((10**n-1)/10)
        nn = p*p
        firsthalf = nn/(10**n)
        
        #chkPalindrome(firsthalf,p,10**n)
        found = False
        
        max = 1
        i = p
        j = p
        f = 0
        pro = firsthalf * ml + reverse(firsthalf)
        #print pro
        
        while firsthalf >ml/10:
            j = p
            toend = pro/j
            #print "toend",toend
            while j >= toend:
                #print "pro",pro,j
                if pro % j == 0:
                    print "fount",pro,j
                    found = True
                    break
                j-=1  
            if found == True:
                break
            firsthalf -=1
            pro = firsthalf * ml + reverse(firsthalf)
            #print pro
            i-=1
        print i,pro    
        #print max
buildTable()        
'''
sol = Solution()
test_data = [ 2]
for d in test_data:
    print sol.largestPalindrome(d)
    
'''   
