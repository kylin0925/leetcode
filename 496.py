class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        print findNums,nums
        res = []
        len_nums = len(nums)
        for n in findNums:
            found = False
            i =0
            while i < len_nums:
                if n == nums[i]:
                    break
                i+=1    
            for j in xrange(i+1,len_nums):            
                if n <nums[j]:
                    res.append(nums[j])
                    found = True
                    break
            if found == False:
                res.append(-1)
        return res        
sol = Solution()
test_data = [[[4,1,2],[1,3,4,2]],[[2,4], [1,2,3,4]],[[1,2], [1,2,3,4]],[[1,2], [4,3,2,1]],[[1,2], [2,7,4,1]] ]
for d in test_data:
    print sol.nextGreaterElement(d[0],d[1])
