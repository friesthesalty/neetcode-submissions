# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if l1 == None and l2 == None: return None

        head = ListNode(0, None)
        
        if l1 == None or l2 == None:
            if l1 == None:
                l1 = ListNode(0, None)
            else:
                l2 = ListNode(0, None)

        s = l1.val + l2.val

        if s >= 10:
            head.val = s % 10
            if l1.next == None:
                l1.next = ListNode(1, None)
            else:
                l1.next.val += 1
        else:
            head.val = s
        head.next = self.addTwoNumbers(l1.next, l2.next)

        return head



        



        