class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """   
        map = {5:0, 10:0, 20:0} #0,5,15 = 10 + 5 = 3 *5
        
        for b in bills:
            change = b - 5
            if change == 0:
                map[5]+=1
                continue             
            elif change == 5:
                if map[5] == 0:
                    #print map, b
                    return False
                else:
                   map[5]-=1
                   map[10]+=1
            elif change == 15:
                map[20]+=1
                if map[5] >=1 and map[10] >=1:                   
                    map[5]-=1
                    map[10]-=1
                elif map[5]>=3:
                    map[5]-=3
                else:
                    #print map, b
                    return False
        #print map            
        return True                    
sol = Solution()
test_data = [[5,5,5,10,20], [10,10], [5,5,10],[5,5,10,10,20]]
for d in test_data:
    print sol.lemonadeChange(d)
