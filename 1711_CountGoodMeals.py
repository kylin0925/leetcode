from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        #import math
        two = [1,2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
                2048, 4096, 8192, 16384, 32768, 65536, 131072,
                262144, 524288, 1048576, 2097152]
        deliciousness.sort()
        nummap = {}
        for i in deliciousness:
            if nummap.get(i) ==None:
                nummap[i]=1
            else:
                nummap[i] += 1
        ans =0
        for i in nummap.keys():
            for t in two:
                tmp = t-i
                if nummap.get(tmp) == None:
                    continue
                if tmp < i:
                    continue
                n = nummap[tmp]
                if tmp == i:
                    ans += n*(n-1)//2 #math.comb(n,2)
                else:
                    ans+=nummap.get(i)*n

        #print("ans", ans)
        return ans % (10**9+7)


#Solution().countPairs(deliciousness = [1,3,5,7,9])
#Solution().countPairs(deliciousness = [1,1,1,3,3,3,7,11,55,56,127])
print(Solution().countPairs(deliciousness = [149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]))
test = [i for i in range(1,10**5)]
#Solution().countPairs(deliciousness = test)