# data = [ [1,2],[3,5],[1,4],[2,3] ]
#
# def cmpf(x):
#     print(x)
#     return x[1]
#
# r = sorted(data,key = cmpf, reverse=True)
# print(r)

res = []
def dfs(text,index):
    global  res

    print("text",text)
    tmp = ""
    cnt = 0

    stack = []
    j=0
    for i in range(0,len(text)):
        print(i,cnt )
        if text[i] == "(":
            cnt+=1
        if text[i] == ")":
            cnt-=1
        if cnt == 0:
            #print("match",cnt,i)
            tmp = "(" + dfs(text[j+1:i], i) + ")"
            print("tmp",tmp)
            stack.append(tmp)
            j=i+1

    print("stack",stack)
    return "".join(stack)

def findFarest(text):
    i = 0
    cnt = 0
    while i < len(text):
        if text[i] == "(":
            cnt+=1
        else:
            cnt-=1
        if cnt == 0:
            return i
    return -1
# def dfs2(text,start,end,stack):
#     print("text",text)
#
#     i = 0
#     res = []
#     tmp = ""
#     while i < end:
#         print("i",i)
#         if text[i] == "(":
#             tmp = "(" +dfs2(text[i+1:],i+1,len(text)-1,res)
#             print("tmp", tmp)
#             res.append(tmp)
#         else:
#             print("return )")
#             return "".join(stack)+")"
#         i+=len(tmp)
#     print("res",res)
#     return  "".join(res)

def makeLargestSpecial(S):
    count = i = 0
    res = []
    print(S)
    for j, v in enumerate(S):
        count = count + 1 if v == '1' else count - 1
        if count == 0:
            res.append('1' + makeLargestSpecial(S[i + 1:j]) + '0')
            print("res",res)
            i = j + 1
    return ''.join(sorted(res)[::-1])
#tmp = dfs("()(()())()",0)
#tmp = makeLargestSpecial("(()(()))")
tmp = makeLargestSpecial("11011000")
#                         11100100
# 1011011000
#
#data = "(()(()))"
#tmp = dfs2(data,0,len(data),[])
print(tmp)