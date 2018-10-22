class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """ 
        def do_filter(s):
            i = 0
            ans = []
            str_len = len(s)
            
            while i < str_len:               
                if s[i]== '#' :
                    if len(ans) > 0:
                        ans.pop()                   
                else:                    
                    ans.append(s[i])
                i+=1
                #print ans
            print "ans",ans
            tmp = [c for c in ans if c != '' ]
            #print tmp
            
            return tmp
            
        return do_filter(S) == do_filter(T)
        
sol = Solution()
test_data = [ ["cca##", "##c"],["ab#c", "ad#c"],["#c", "ad#c"],['#','#'],['abc#','abf#'],['#abc','#abc'],['a#b#cd','cd']]
for d in test_data:
    print sol.backspaceCompare(d[0],d[1])
