# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1 = l1
        t2 = l2
        c = 0
        ans = None
        head = None
        while t1!=None or t2!=None:
            n = 0
            if t1!=None:
                n = t1.val
            if t2 != None:
                n = n + t2.val
            n = n + c
            c = n /10
            n = n % 10
            #print n,c
            if ans ==None:
                ans = ListNode(n)
                head = ans
            else:
                tmp = ListNode(n)
                ans.next = tmp
                ans = tmp       
            if t1!=None:
                t1 = t1.next
            if t2!=None:
                t2 = t2.next
        
        if c >0:
            tmp = ListNode(c)
            ans.next = tmp
            ans = tmp       

        return head
        