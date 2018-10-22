class Solution(object):
    def sumxy(self,nums,start,end):
        acc = 0
        #print "sumxy",start,end
        for i in range(start,end):
            acc +=nums[i]
        return acc
        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        
        start = 0
        end = 1
        max_sum = 0
        nums_len = len(nums)
        if nums_len == 0:
            return []
        max_sum = nums[0]
        for i in range(1,nums_len+1):
            #print "len",i
            for start in range(nums_len-i+1):
                #print "start",start,start+i
                r = self.sumxy(nums,start,start+i)
                #print r
                if r >max_sum:
                    max_sum = r
                
        return max_sum
sol = Solution()
test_data = [ [-2,1,-3,4,-1,2,1,-5,4],[1,2,7],[-1,-1,1,9],[],[1],[0,0],[-1,-1],[-2,1]]
#test_data = [ [1,2]]
for d in test_data:
    print sol.maxSubArray(d)
