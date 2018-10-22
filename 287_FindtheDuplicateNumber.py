class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maplist = [0 for x in range(n)]
        for i in nums:
            maplist[i] +=1

        for i in range(n):
            if maplist[i] >1:
                return i
        return  0

sol = Solution()
test_data = [[1,3,4,2,2], [3,1,3,4,2],[1,1],[1,1,2,3],[2,2,2,2]]
for d in test_data:
    print(sol.findDuplicate(d))