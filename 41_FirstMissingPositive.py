class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}
        maxnum = 1
        for i in nums:
            numMap[i] = 1
            if maxnum < i:
                maxnum = i
        #print(numMap,maxnum)
        maxnum +=1

        for i in range(1,maxnum+1):
            if i not in numMap:
                return i

sol = Solution()

data = [ [0, 2, 1],[7,8,9,11,12],[3,4,-1,1]]
for d in data:
    print(sol.firstMissingPositive(d))