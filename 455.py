class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        g_len = len(g)  
        s_len = len(s)

        res = 0
        #print "start"
        i =0
        j =0
        while i < g_len and j < s_len:
            #print i,j
            if g[i] <= s[j]:
                res+=1
                i+=1
                j+=1
            elif g[i] > s[j]:
                j+=1
            
        return res            
                    
sol = Solution()
test_data = [ [[10,9,8,7],[5,6,7,8]],[[1,2,3],[3,2,1] ] , [ [1,2], [1,2,3]],[[1,2,3],[1,1]],[[2],[1]]]
for d in test_data:
    print sol.findContentChildren(d[0],d[1])
