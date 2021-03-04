# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        self.targetnode = []
        def find(node,value):
            if node == None:
                return
            if node.val == value:
                self.targetnode.append(node)
                #return
            find(node.left,value)            
            find(node.right,value)
            #return res
        
        def cmpTree(s,t):
            if s ==None or t == None:
                #print("return",s==t)
                return s == t
            if s.val == t.val:
                r = cmpTree(s.left,t.left)
                r1 = cmpTree(s.right,t.right)
                return r and r1
            else:
                #print(s,t)
                return False
        find(s,t.val)
        #print(self.targetnode)
        for n in self.targetnode:
            if n !=None:
                r = cmpTree(n,t)
                if r:
                    return True
        
        return False
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def dfs(s,t): #leetcode 100
            if s == None or t == None:
                return t==s
            return dfs(s.left,t.left) and dfs(s.right,t.right) and s.val == t.val
        
        def dfs2(s,t):
            if s == None or t ==None:
                return s==t
            if dfs(s,t):
                return True
            else:
                return dfs2(s.left,t) or dfs2(s.right,t)
        return dfs2(s,t) 
                