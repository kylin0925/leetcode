class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 =="0" or num2 =="0":
            return "0"
        map_char = {'1':1,
                    '2':2,
                    '3':3,
                    '4':4,
                    '5':5,
                    '6':6,
                    '7':7,
                    '8':8,
                    '9':9,
                    '0':0}
        charlist = ['0','1','2','3','4','5', '6', '7', '8', '9']
        def toIntList(num):
            inum = []
            for d in num:
                inum.append(map_char[d])
            return inum

        def mul(n1,l1,n2,l2):
            n1 = n1[::-1]
            n2 = n2[::-1]

            res=[0 for i in range(l1+l2)]
            carry = 0
            j=0
            for c in n2:
                i=0
                for c1 in n1:
                    tmp = res[i+j] +c*c1+carry
                    carry = tmp//10
                    res[i+j] = tmp %10
                    i+=1
                if carry > 0:
                    res[i+j] = carry
                carry = 0
                j += 1
                #print(res)

            if carry > 0:
                res[-1] = carry
            if res[-1] == 0:
                del res[-1]
            return res[::-1]

        def IntListToStr(intlist):
            res = []
            for i in intlist:
                res.append(charlist[i])

            return res
        n1=n2=[]
        l1 = len(num1)
        l2 = len(num2)
        if l1>=l2:
            n1 = toIntList(num1)
            n2 = toIntList(num2)
        else:
            n1 = toIntList(num2)
            n2 = toIntList(num1)
            l1,l2 = l2,l1

        res = mul(n1,l1,n2,l2)
        #print(n1)
        #print(n2)
        #print(res)
        ans = "".join(IntListToStr(res))
        return ans

sol = Solution()

print(sol.multiply("10","10"))