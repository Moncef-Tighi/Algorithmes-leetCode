"""ça c'est le code qui m'a apprit à utiliser les Linked List, tout est fait par moi.
Le principe que j'avais pas compris c'est que les pointers ne sont PAS des variables
quand on fait des modifications sur la liste, si on appel le pointer original ces modifications là seront appliqués"""
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current=list1
        previous=None
        i=a
        while current:
            if a<1:
                newHead=previous
                while i<b:
                    current=current.next
                    i+=1                    
                tail=current.next
                newHead.next=list2
                while newHead.next!=None:
                    newHead=newHead.next
                newHead.next=tail
                return list1
            previous=current
            current=current.next
            a-=1