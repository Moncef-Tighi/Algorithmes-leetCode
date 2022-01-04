# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""Alors le problème c'est qu'il faut ittérer à travers la LinkedList sans l'écraser au passage avec un head= head.next malencontreux.
Je suis même plus sûr de comment j'ai fait mais apparamment c'est la solution opti"""

class Solution:
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        holder=head
        if not head:
            return head
        while head.next:
            if head.next and head.val==head.next.val:
                if holder.next.next==None:
                    holder.next=None
                else:
                    head.next=head.next.next
            else:
                head = head.next
        return holder