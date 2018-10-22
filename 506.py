class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        tmp = [i for i in nums]
        tmp.sort(reverse=True)
        #print tmp,nums
        nums_len = len(nums)
        i = 0
        res = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        dictmap = {}
        i = 0
        while i < len(tmp):
            if i <3:
                dictmap[tmp[i]] = res[i]
            else:
                dictmap[tmp[i]] = str(i+1)
            i+=1 
        res = []
        for n in nums:
            res.append(dictmap[n])
        #print dictmap        
        return res    
sol = Solution()
test_data = [  [10,3,8,9,4],[5,4,3,2,1],[6,7,8]]
for d in test_data:
    print sol.findRelativeRanks(d)
