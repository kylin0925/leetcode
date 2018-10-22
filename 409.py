class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """  
        table = [0 for i in xrange(256)]
        res_len =0        
        one_flag = 0
        for c in s:
            if table[ord(c)] == 0:
                cnt = s.count(c)
                if cnt % 2 == 0:
                    res_len +=cnt
                else:
                    if cnt == 1:
                        one_flag = 1
                    else:    
                        res_len +=cnt-1
                        one_flag = 1
                table[ord(c)] =cnt
           
        return res_len + one_flag
sol = Solution()
test_data = ["a","abccccdd","aaabbb",'ccc']
for d in test_data:
    print sol.longestPalindrome(d)
