class Solution2:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        lenrow = len(row) >> 1
        pos = [x for x in range(lenrow)]
        def dfs(i):

            print("intput i",i)
            if pos[i] == i:
                return i
            else:
                pos[i] = dfs(pos[i])

            return pos[i]


        cnt = lenrow
        for i in range(0,lenrow):
            a = dfs(row[2*i]>>1)
            b = dfs(row[2*i+1]>>1)
            #print(a,b)
            if a != b:
                pos[a]=b
                cnt-=1


        return cnt

class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        lenrow = len(row)
        cnt =0
        for i in range(0,lenrow-1,2):

            if row[i] &1 == 1:
                target =row[i] - 1
            else:
                target = row[i] +1
            #print(row[i],target)
            if row[i+1] == target:
                continue

            for j in range(i+1,lenrow):
                if row[j] == target:
                    tmp = row[i+1]
                    row[i+1] = row[j]
                    row[j] = tmp
                    cnt +=1
                    break
            #print(row)
        #print("cnt",cnt)
        return cnt
sol = Solution()

data = [ [0, 2, 1, 3],[3, 2, 1, 0],[5,4,2,6,3,1,0,7]]
#data = [ [6,2,1,7,4,5,3,8,0,9]]
for d in data:
    print(sol.minSwapsCouples(d))