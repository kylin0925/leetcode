class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        table = [ 0 for x in range(len(seats))]
        i = 0
        cnt = 0
        while i < len(seats):
            if seats[i] == 1:
                cnt = 0
                table[i] = 0
            else:
                cnt+=1
                table[i] = cnt               
            i+=1
        print table

        cnt = 0
        i = len(seats) -1
        while i >= 0 :
            if seats[i] == 1:
                cnt = 0
                table[i] = 0
            else:
                cnt+=1
                if i == len(seats) -1 or i == 0:
                    table[i] = max(table[i],cnt)
                else:
                    table[i] = min(table[i],cnt)
            i-=1  
        #print table
        return max(table)
sol = Solution()
test_data = [[1,0,0,0,1,0,1],[1,0,0,0],[0,0,1] ]
for d in test_data:
    print sol.maxDistToClosest(d)
