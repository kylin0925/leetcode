class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #print s,p
        if p =="":
            #print "pattern is empty"
            return s == ""
            
        if (len(p)>=2 and p[1]!='*') or len(p)==1:
            r = (len(s)>=1 and (p[0] == s[0]) or ((p[0] == '.') and len(s) >=1))
            #print "first ch is match " ,r
            return r and self.isMatch(s[1:],p[1:])
        
        #print "match next is * ","text",s,"pattern",p
        
        while (len(p)>=1 and len(s)>=1 and p[0] == s[0]) or ((len(p)>=1) and p[0] == '.'):
            if self.isMatch(s,p[2:]):
                return True
            #print "match p[2] complete incres s",s,p    
            s = s[1:]
            if s =="":
                break
        #print "match s",s,"p[2:]",p[2:]
        return self.isMatch(s,p[2:])
        
#s = "mississippi"
#p = "mis*is*p*."
#s = "mississippi"
#p = "mis*is*p*."
s = "aa"
p = "a*"
test_data = [["mississippi" , "mis*is*ip*."] , 
                ["abc","abc"],
                ["a","a*"],
                ["abc","ab."],
                ["","abc"],
                ["",".*"],
                ["abc","a*b*c*"],
                ["a","a*b*c*"],
                ["a","c*"],
                ["aab","c*a*b"],
                ["mississippi","mis*is*ip*."], 
                ["a",".*..a*"],
                ["aaaaabaccbbccababa","a*b*.*c*c*.*.*.*c"]
                ]
sol = Solution()
for data in test_data:
    print "test data",data
    print sol.isMatch(data[0],data[1])