# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        p = dummy_head = ListNode(0)
        dummy_head.next = head

        while p.next != None and p.next.next!=None:
            a = p.next
            b = p.next.next
            #print(a.val,b.val)

            tmp = b.next
            p.next = b
            b.next = a
            a.next =tmp
            p =a

        #dump(dummy_head.next)

        return dummy_head.next


def makeList(data):
    head = None
    tmp = None
    for d in data:
        if head==None:
            head = ListNode(d)
            tmp = head
        else:
            node = ListNode(d)
            tmp.next = node
            tmp = tmp.next
    return head

def dump(head):
    tmp = head
    while tmp !=None:
        print(tmp.val)
        tmp = tmp.next

head = makeList([])
#print(head)
#dump(head)

sol = Solution()
h = sol.swapPairs(head)
print("result")
dump(h)