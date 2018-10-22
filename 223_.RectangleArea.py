class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        l_b_x = max(A,E)
        l_b_y = max(B,F)
        
        r_t_x = min(C,G)
        r_t_y = min(D,H)
        
        print l_b_x, l_b_y, r_t_x, r_t_y
        ow = (r_t_x - l_b_x)
        oh = (r_t_y - l_b_y) 
        overlap = (r_t_x - l_b_x) * (r_t_y - l_b_y) 
        if ow < 0 or oh <0:
            overlap = 0
        r1_area = (C - A) * (D-B)
        r2_area = (G - E) * (H-F)
        
        return r1_area + r2_area - overlap
sol = Solution()
test_data = [ [ -3, 0, 3, 4, 0, -1, 9, 2] ]
for d in test_data:
    print sol.computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
