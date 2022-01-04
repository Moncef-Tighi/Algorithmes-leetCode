class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left==right:
            return head
        previous=None
        current=head
        i=right-left
        j=1
        while current:
            if j==left:
                #La partie qui fait l'inversion
                newHead=previous
                tail=current
                while i>=0:
                    holder=current.next
                    current.next=previous
                    previous=current
                    current=holder
                    i-=1
                #Pas trop compris ce code
                if newHead:
                    newHead.next=previous
                else:
                    head=previous
                tail.next=current
                return head

            
            else:
                j+=1
                previous=current
                current=current.next
        return previous