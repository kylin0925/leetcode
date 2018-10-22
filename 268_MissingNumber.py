class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        a = sum(nums)
        b = (1 + n) *n/2
        return int(b-a)

sol = Solution()
test_data = [[3,0,1],[9,6,4,2,3,5,7,0,1],[1,2,3],[1],[0],[0,1]]
for d in test_data:
    print(sol.missingNumber(d))
