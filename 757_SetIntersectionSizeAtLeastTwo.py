class Solution:
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """


        intervals.sort(key=lambda x:x[1])
        #print(intervals)
        m=0
        largest_1 = -1
        largest = -1
        for interval in intervals:
            p1,p2 = interval
            #print("largest ",largest,largest_1)
            if p1 <= largest and p1 <=largest_1:
                continue
            if p1 <=largest and p1 > largest_1:
                m+=1
                largest_1 = largest
            if p1 > largest:
                m+=2
                largest_1 = p2 -1

            largest = p2
        return m
sol = Solution()
test_data = [ [ [1,2],[4,5],[2,4],[2,3] ] ,
              [ [1,3], [1,4], [2,5], [3,5]]
              ]
for d in test_data:
    print(sol.intersectionSizeTwo(d))