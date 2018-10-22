class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False 
         
        s = str(x)
        tmp = s[::-1]
        #print tmp
        if x <0:           
            tmp = tmp[0:-1]
            tmp = "-" + tmp
            
        #print tmp,s
        tmpi = int(tmp)
        return tmp == s
a = Solution()
print a.isPalindrome(-2147447412) == False


print a.isPalindrome(31) == False

print a.isPalindrome(77) == True

print a.isPalindrome(-3) == True

print a.isPalindrome(3) == True