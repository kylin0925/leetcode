class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        table = [1,4,16,64,256,1024,4096,16384,65536,262144,1048576,4194304,16777216,67108864,268435456,
                    1073741824,4294967296,17179869184]
        return num in table            
sol = Solution()
test_data = [ -1,-333,1,2,3,4,5,6,7,8,10,100,65536]
for d in test_data:
    print sol.isPowerOfFour(d)
