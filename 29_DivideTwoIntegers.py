class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #print(dividend,divisor)
        q = 0
        signFlag = 1 if dividend < 0 else 0
        signFlag2 = 1 if divisor < 0 else 0
        s = 0
        if signFlag != signFlag2:
            s =1
        if dividend < 0:
            dividend = (~dividend) +1

        if divisor < 0:
            divisor = (~divisor) +1
        divisor = divisor << 32
        for i in range(33):
            dividend = dividend - divisor
            if dividend >=0:
                q = q << 1
                q = q | 1
            else:
                dividend += divisor
                q = q <<1
            divisor = divisor>>1

        #print(q, dividend)
        if signFlag == signFlag2:
            q = 2147483647 if q > 2147483647 else q

        if  s ==1:
            #q+=1
            q = ~q +1
        #print(q,dividend)

        return q

sol = Solution()
test_data = [[-2147483648,1],[7,-3],[-10,2],[10,5]]
for d in test_data:
    print(sol.divide(d[0],d[1]))
