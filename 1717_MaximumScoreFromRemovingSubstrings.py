class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # ab and gain  x  points
        # ba and gain  y  points.
        score = []
        if x>y:
            score.append(["ab",x])
            score.append(["ba", y])
        else:
            score.append(["ba", y])
            score.append(["ab", x])


        stack = []
        total = 0
        i = 0
        for c in s:
            if c == 'a' or c == "b":
                if len(stack) == 0:
                    stack.append(c)
                else:
                    tmp = stack[-1] + c
                    if tmp == score[0][0]:
                        total += score[0][1]
                        stack.pop()
                    else:
                        stack.append(c)
            else:
                stack2= []
                for c in stack:
                    if len(stack2) == 0:
                        stack2.append(c)
                    else:
                        tmp = stack2[-1]+c
                        if tmp == score[1][0]:
                            total += score[1][1]
                            stack2.pop()
                        else:
                            stack2.append(c)
                stack=[]

        if len(stack)!=0:
            stack2 = []
            for c in stack:
                if len(stack2) == 0:
                    stack2.append(c)
                else:
                    tmp = stack2[-1] + c
                    if tmp == score[1][0]:
                        total += score[1][1]
                        stack2.pop()
                    else:
                        stack2.append(c)
        return total



print(Solution().maximumGain(s = "aabbaaxybbaabb", x = 5, y = 4))
print(Solution().maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))
print(Solution().maximumGain(s = "aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha", x = 1926, y = 4320))

print(Solution().maximumGain(s = "aabbabk", x = 5, y = 125))
'''
"aabbabk"
ab 5
ba 125

'''



