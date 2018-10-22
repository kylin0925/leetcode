class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            m = [0 for i in range(256)]
            for c in A:
                m[ord(c)] +=1                
            
            for i in m:
                if i >=2:
                    return True
            return False
        a_len = len(A)
        b_len = len(B)
        if a_len != b_len:
            return False
        i = 0
        diff_pos = []
        while i < a_len:
            if A[i]!=B[i]:
                diff_pos.append(i)
            i+=1    
        if len(diff_pos) != 2:
            return False
        
        tmp = [c for c in A]
        t = tmp[diff_pos[0]]
        tmp[diff_pos[0]] = tmp[diff_pos[1]] 
        tmp[diff_pos[1]] = t
        tmp = "".join(tmp)
        if tmp!=B:
            return False
        else:
            return True
sol = Solution()
test_data = [ ["","ab"],["ab","cd"],["aa","aa"], ["ab","ab"], ["ab","ba"], [ "aaaaaaabc", "aaaaaaacb"]]
for d in test_data:
    print sol.buddyStrings(d[0], d[1])
