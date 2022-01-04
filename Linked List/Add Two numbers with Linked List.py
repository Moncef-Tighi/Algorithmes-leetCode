# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = current = ListNode(0)
        holder = 0
        while l1 or l2 or holder:
            if l1:
                holder += l1.val
                l1 = l1.next
            if l2:
                holder += l2.val
                l2 = l2.next
            current.next = ListNode(holder%10)
            current = current.next
            holder= holder//10
        return l3.next