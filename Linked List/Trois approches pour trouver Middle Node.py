"""Trouver la middleNode en trouvant la maximum et en ittérant une deuxième fois sur la linked List pour trouver le centre
(ma solution)"""

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i=0
        root=head
        while root.next:
            i+=1
            root=root.next
        root=head
        middle=i//2
        while i>0:
            root=root.next
            i-=1
            if i==middle:
                return root
        return root


"""Stratégie du lièvre et de la tortue : (meilleur solution)
When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast.
 When fast reaches the end of the list, slow must be in the middle.
"""

class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


"""Traverser la Linked List et mettre les nodes dans un Array:
Put every node into an array A in order. Then the middle node is just A[A.length // 2], since we can retrieve each node by index.

We can initialize the array to be of length 100, as we're told in the problem description that the input contains between 1 and 100 nodes."""

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]