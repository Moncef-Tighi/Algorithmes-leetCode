# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited=[]
        if not head:
            return False
        while head.next:
            if head in visited:
                return True
            else:
                visited.append(head)
                head=head.next
        return False
            
"""Solution brillante:

Took 88 ms and the "Accepted Solutions Runtime Distribution" doesn't show any faster Python submissions. The "trick" is to not check all the time whether we have reached the end but to handle it via an exception. "Easier to ask for forgiveness than permission."

The algorithm is of course Tortoise and hare.

def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

# Explication  :

This is pretty classical and well-know problem about linked list. One way is just to put all linked list to for example hash table and check if we have repeating elements. However it will take O(n) space. There is better solution with only O(1) complexity. Imagine the following example:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3, the list with loop. Idea is to use two pointers, one is slow and one is fast, let us do several steps:

At the beginning, both of them at number 1.
Next step, slow pointer at 2 and fast at 3.
Next step, slow pointer at 3 and fast at 5.
Next step, slow pointer at 4 and fast at 3.
Next step, slow pointer at 5 and fast is also 5, so we have the same element and we return True.
If we do not have loop we will never have equal elements, if we have loop, because slow pointer moves with speed 1 and fast with speed 2, fast pointer will always gain slow one.


"""