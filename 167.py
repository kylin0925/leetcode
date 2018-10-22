class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        nums_len = len(numbers)
        start = 0
        end = nums_len -1
        if start == end:
            return numbers
            
        while start < end:
            if numbers[start] + numbers[end] <target:
                start +=1
            elif numbers[start] + numbers[end] > target:    
                end -=1
            else:
                return [start+1,end+1]
        return []       
sol = Solution()
test_data = [ [[2,7,11,15],9],[[-7,-2,11,15],13] ]
for d in test_data:
    print sol.twoSum(d[0],d[1])
