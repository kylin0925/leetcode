# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sortlist = []
        def traversal(root):

            if root == None:
                return

            traversal(root.left)
            #print(root.val)
            sortlist.append(root.val)
            traversal(root.right)
        traversal(root)
        #print(sortlist)
        min = sortlist[1] - sortlist[0]
        for i in range(2,len(sortlist)):
            if min > (sortlist[i] - sortlist[i-1]):
                min = sortlist[i] - sortlist[i-1]
        return  min
import binaryTree

sol = Solution()

root = binaryTree.buildTestBST([4,2,6,1,3])
print("sol")
print(sol.minDiffInBST(root))
#test_data = []
#for d in test_data:
#    pass
