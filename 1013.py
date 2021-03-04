class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_a = sum(A)
        target = sum_a //3
        
        cnt = len(A)
        res= [x for x in A]
        i = 1
        while i < cnt:
            res[i] = res[i] + res[i-1]
            i+=1
        i = 0
        
        pos = [0,0]
        
        for x in range(2):
            while i < cnt:
                if res[i] == target:
                    break
                i+=1
            if i >= cnt:
                return False
            print(i)   
            pos[x]=i+1
            i=0
            while i < cnt:
                res[i]-=target
                i+=1
            i = pos[x]
        print(sum(A[pos[1]:]))
        if sum(A[pos[1]:]) == target and pos[0] < pos[1] and pos[1] < cnt :
            return True
        else:
            return False