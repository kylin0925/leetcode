class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
	
class Solution(object):
    def invert(self,node):
        if node != None:
		    tmp = node.left
		    node.left = node.right
		    node.right = tmp
		    self.invert(node.left)
		    self.invert(node.right)
		    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
		
def invert(node):
	if node != None:
		tmp = node.left
		node.left = node.right
		node.right = tmp
		invert(node.left)
		invert(node.right)
def dump(node):
	if node.left !=None:
		dump(node.left)
	print node.val
	if node.right !=None:
		dump(node.right)
		
root = TreeNode(4)
l = TreeNode(3)
r = TreeNode(5)
root.left = l
root.right = r
t1 = TreeNode(1)
t2 = TreeNode(2)
l.left = t1
l.right = t2
print root.val, root.left.val, root.right.val
dump(root)
#invert(root)
#print "================"
#dump(root)


s = Solution()
s.invertTree(root)

print "================"
dump(root)