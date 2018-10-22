class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """  
        l_b_x = max(rec1[0],rec2[0])
        l_b_y = max(rec1[1],rec2[1])
        
        r_t_x = min(rec1[2],rec2[2])
        r_t_y = min(rec1[3],rec2[3])
        
        #print l_b_x, l_b_y, r_t_x, r_t_y
        #print (r_t_x - l_b_x)
        #print (r_t_y - l_b_y) 
        
        return ((r_t_x - l_b_x) * (r_t_y - l_b_y) > 0) and (r_t_x - l_b_x) > 0 and(r_t_x - l_b_x)>0
sol = Solution()
test_data = [   #[[0,0,2,2], [1,1,3,3]], 
                #[[0,0,2,2], [2,0,4,2]], 
                #[[1,1,3,3], [0,0,2,2]],
                #[[0,0,1,1], [1,0,2,1]],
                #[[0,0,5,5], [1,1,2,2]],
                #[[0,0,5,5], [5,0,7,2]],
                #[[1,1,5,5], [5,0,7,2]],
                #[[1,1,5,5], [5,5,7,7]],
                
                [[0,0,1,1], [2,2,3,3]], 
                [[0,5,2,7], [1,0,3,3]], 
                
                ]
for d in test_data:
    print sol.isRectangleOverlap(d[0],d[1])
