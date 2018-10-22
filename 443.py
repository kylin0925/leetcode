class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """   
        dict = {}
        res = []
        i = 0
        while i < len(chars):
            #print "1",i,chars[i]
            cnt = 1
            j = i+1
            while j < len(chars):
                if chars[i] == chars[j]:
                    cnt +=1
                else:
                    break
                j+=1    
            #print i,"cnt",cnt 
            res.append(chars[i])
            if cnt > 1:
                for c in str(cnt):
                    res.append(c)
            i+=cnt
        i = 0
        while i < len(res):
            chars[i] = res[i]
            i+=1
        return i
sol = Solution()
test_data = [["a"],["a","a","b","b","c","c","c"],['a','a','a','a','a','a','a','a','a','a'] ]
for d in test_data:
    print sol.compress(d),d
    