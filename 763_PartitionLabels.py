class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def isLast(S,start):
            c = S[start]
            #print("is last ",c)
            for i in range(start+1,len(S)):
                if c == S[i]:
                    return False
            return True


        def check(S,start,i,end):

            left = S[start:i+1]
            right = S[i+1:end]
            #print(S, len(left),left,right)
            for c in left:
                if c in right:
                    return False
            return True

        res = []
        start = 0
        end = len(S)

        i = 0
        while i < end:
            c = S[i]
            #print(c,isLast(S,i))
            if isLast(S,i):
                if check(S,start,i,end):
                    res.append(i+1-start)

                    #print("update start",start,i)
                    start = i + 1
            i+=1
        return res
sol = Solution()
test_data = ["ababcbacadefegdehijhklij"]
for d in test_data:
    print(sol.partitionLabels(d))