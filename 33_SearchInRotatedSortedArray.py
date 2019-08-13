class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(target,nums,start,end):
            while start <= end:
                mid = start + int((end-start)/2)
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    start = mid +1
                else:
                    end = mid-1
            return -1
        left =0
        nums_len = len(nums)
        if nums_len == 0:
            return -1
        right = nums_len -1
        # find smallest nums
        mid = 0
        while left < right:
            mid = int((right + left)/2)
            if nums[mid] > nums[right]:
                left = mid +1
            else:
                right=mid
        #print(nums,"debug mid is ",left, mid)

        right = nums_len - 1
        if target >= nums[left] and target <= nums[right]:
            ans = binarySearch(target,nums,left,right)
        else:
            ans =binarySearch(target,nums, 0,left-1)
        return ans
sol = Solution()

data = [ [[4,5,6,7,0,1,2],0],
            [[1,2,5,0],1],
            [[0,1,2,5],4],
         [[1,2,3],1],
         [[1,2,3],2],
         [[1,2,3],3],
         [[2,3,1],2],
         [[2,3,1],3],
[[4,5,7,8,9,10,1,2,3],1],
[[4,5,7,8,9,10,1,2,3],4],
[[4,5,7,8,9,10,1,2,3],411],
[[4,5,7,8,9,10,1,2,3],3],
[[4,5,7,8,9,10,1,2,3],2],
[[4,5,7,8,9,10,1,2,3],1],
[[4,5,7,8,9,10,1,2,],1],
[[4,5,7,8,9,10,1,2,],2],
         [[1],1],
         [[],1],
         [[0],12],
         [[2,1],1],
         [[2,1],2]
         ]
#data = [  [[2,1],1] ]

for d in data:
    ans = sol.search(d[0],d[1])
    print("ans ",ans)
