class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        nums.sort()
        n = nums[0]
        num = nums[0]
        result = num
        max_num_len = 1
        tmp_cnt =1
        i = 1
        nums_len = len(nums)
        #print nums,nums_len
        while i < nums_len:
            #print "loop",tmp_cnt,nums[i],num
            if nums[i] != num :
                if tmp_cnt > max_num_len:
                    max_num_len = tmp_cnt   
                    result = num        
                    #print "update max ",max_num_len
                num=nums[i]    
                tmp_cnt =1    
            else:
                tmp_cnt+=1
            i+=1
        if tmp_cnt > max_num_len:    
            max_num_len = tmp_cnt  
            result = nums[-1]
        #print result    
        return result        
sol = Solution()
test_data = [ [3,2,3], [2,2,1,1,1,2,2] ,[1,2,2,2,3],[1,4,2,3,1] ]
for d in test_data:
    print sol.majorityElement(d)
