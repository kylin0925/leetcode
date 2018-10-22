class NumArray(object):
    table = []
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.table = []
        nums_len = len(nums)
        if nums_len > 1:
            self.table.append(nums[0])
        else:
            self.table = nums
            return
        for x in xrange(1,nums_len):
            self.table.append( nums[x] + self.table[x-1])
        #print self.table
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """  
        if len(self.table) ==0:
            return 0
        if len(self.table) ==1:
            return self.table[0]
        if i > 0:    
            return self.table[j] - self.table[i-1] 
        else:
            return self.table[j]
#sol = Solution()

test_data = [ [-4, -5]]
test_data2 = [ [0,0] ,[0, 1,],]
for d in test_data:
    sol = NumArray(d)
    for r in test_data2:
        print sol.sumRange(r[0],r[1])
